#!/usr/bin/env python3
# coding: utf-8
# File: build_graph.py
# Author: Suriel
# Date: 20-6-24

import os
import json
from py2neo import Graph, Node


class Graph:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        self.data_path = os.path.join(cur_dir, 'data/place.json')
        self.data_path2 = os.path.join(cur_dir, 'data/measure.json')
        self.g = Graph(
            host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            http_port=7474,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="mima1234")
        print("connect successful")

    '''读取文件'''

    def read_nodes(self):
        # 共6类节点 13+1
        print("read_nodes")
        # 地点
        places = []
        # 类型
        types = []
        # 区域
        areas = []
        # 措施
        low_measures = []
        mid_measures = []
        hig_measures = []

        place_infos = []

        # 构建节点实体关系
        # 地点与类型关系
        rels_place_type = []
        # 地点与区域关系
        rels_place_area = []
        # 类型和措施关系
        rels_type_lowmeasure = []
        rels_type_midmeasure = []
        rels_type_higmeasure = []

        count = 0
        for data in open(self.data_path, encoding='utf-8'):
            place_dict = {}
            count += 1
            print(count)
            # 知识图谱属性类型 10
            data_json = json.loads(data)
            # data_json = demjson(data_json)
            place = data_json['name']
            place_dict['name'] = place
            places.append(place)
            place_dict['tel'] = ''
            place_dict['address'] = ''
            # 读取属性值
            if 'tel' in data_json:
                place_dict['tel'] = data_json['tel']
            if 'address' in data_json:
                place_dict['address'] = data_json['address']
            if 'type' in data_json:
                ptype = data_json['type'].split(';')[0]
                # print(ptype)
                rels_place_type.append([place, ptype])
                types += ptype.split()
            # print(types)
            if 'business_area' in data_json:
                area = data_json['business_area']
                # print(area)
                rels_place_area.append([place, area])
                areas += area.split()
            # print(areas)
            place_infos.append(place_dict)
            # print(set(types))
        for data2 in open(self.data_path2, encoding='utf-8'):
            data_json = json.loads(data2)
            ptype = data_json['type']
            if 'low_measure' in data_json:
                low_measure = data_json['low_measure']
                # print(low_measure)
                rels_type_lowmeasure.append([ptype, low_measure])
                low_measures.append(low_measure)
            # print(low_measures)
            if 'mid_measure' in data_json:
                mid_measure = data_json['mid_measure']
                # print(mid_measure)
                rels_type_midmeasure.append([ptype, mid_measure])
                mid_measures.append(mid_measure)
            # print(mid_measures)
            if 'hig_measure' in data_json:
                hig_measure = data_json['hig_measure']
                # print(hig_measure)
                rels_type_higmeasure.append([ptype, hig_measure])
                hig_measures.append(hig_measure)
            # print(hig_measures)
        return set(places), set(types), set(areas), set(low_measures), set(mid_measures), set(hig_measures), place_infos, rels_place_type, rels_place_area, rels_type_lowmeasure, rels_type_midmeasure, rels_type_higmeasure

    '''建立节点'''

    def create_node(self, label, nodes):
        count = 0
        for node_name in nodes:
            node = Node(label, name=node_name)
            self.g.create(node)
            count += 1
            print(count, len(nodes))
        return

    '''创建地点中心节点'''

    def create_places_nodes(self, place_infos):
        count = 0
        for place_dict in place_infos:
            node = Node(
                "places", name=place_dict['name'], tel=place_dict['tel'], address=place_dict['address'])
            self.g.create(node)
            count += 1
            print(count)
        return

    '''创建实体节点类型'''

    def create_graphnodes(self):
        # 修改
        places, types, areas, low_measures, mid_measures, hig_measures, place_infos, rels_place_type, rels_place_area, rels_type_lowmeasure, rels_type_midmeasure, rels_type_higmeasure = self.read_nodes()
        self.create_places_nodes(place_infos)
        self.create_node('types', types)
        self.create_node('areas', areas)
        self.create_node('low_measures', low_measures)
        self.create_node('mid_measures', mid_measures)
        self.create_node('hig_measures', hig_measures)
        return

    '''创建实体关系边'''

    def create_graphrels(self):
        print("************************************************")
        # 修改
        places, types, areas, low_measures, mid_measures, hig_measures, place_infos, rels_place_type, rels_place_area, rels_type_lowmeasure, rels_type_midmeasure, rels_type_higmeasure = self.read_nodes()
        self.create_relationship(
            'places', 'types', rels_place_type, 'belongs_to', '所属类型')
        self.create_relationship(
            'places', 'areas', rels_place_area, 'belongs_to', '所属区域')
        self.create_relationship(
            'types', 'low_measures', rels_type_lowmeasure, 'suggest', '低级防控建议')
        self.create_relationship(
            'types', 'mid_measures', rels_type_midmeasure, 'suggest', '中级防控建议')
        self.create_relationship(
            'types', 'hig_measures', rels_type_higmeasure, 'suggest', '高级防控建议')

    '''创建实体关联边'''

    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        count = 0
        # 去重处理
        set_edges = []
        for edge in edges:
            set_edges.append('###'.join(edge))
        all = len(set(set_edges))
        for edge in set(set_edges):
            edge = edge.split('###')
            p = edge[0]
            q = edge[1]
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (
                start_node, end_node, p, q, rel_type, rel_name)
            try:
                self.g.run(query)

                count += 1
                print(query)
                print(rel_type, count, all)
            except Exception as e:
                print(e)
        return

    '''导出数据'''

    def export_data(self):
        places, types, areas, low_measures, mid_measures, hig_measures, place_infos, rels_place_type, rels_place_area, rels_type_lowmeasure, rels_type_midmeasure, rels_type_higmeasure = self.read_nodes()
        fplaces = open('places.txt', 'w+')
        ftypes = open('ftypes.txt', 'w+')
        fareas = open('areas.txt', 'w+')
        flow_measures = open('low_measures.txt', 'w+')
        fmid_measures = open('mid_measures.txt', 'w+')
        fhig_measures = open('hig_measures.txt', 'w+')

        fplaces.write('\n'.join(list(places)))
        ftypes.write('\n'.join(list(types)))
        fareas.write('\n'.join(list(areas)))
        flow_measures.write('\n'.join(list(low_measures)))
        fmid_measures.write('\n'.join(list(mid_measures)))
        fhig_measures.write('\n'.join(list(hig_measures)))
        fplaces.close()
        ftypes.close()
        fareas.close()
        flow_measures.close()
        fmid_measures.close()
        fhig_measures.close()

        return


if __name__ == '__main__':
    handler = Graph()
    handler.create_graphnodes()
    handler.create_graphrels()
    handler.export_data()
