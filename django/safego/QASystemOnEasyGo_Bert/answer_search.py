#!/usr/bin/env python3
# coding: utf-8
# File: answer_search.py
# Author: Suriel
# Date: 20-6-18

from py2neo import Graph
from run_similarity import BertSim
import io
import re
import time
import jieba
import numpy as np
import pandas as pd
import urllib.request
import urllib.parse
import tensorflow as tf
import os
bs = BertSim()
bs.set_mode(tf.estimator.ModeKeys.PREDICT)

os.environ['CUDA_VISIBLE_DEVICES'] = '3'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


class AnswerSearcher:
    def __init__(self):
        self.g = Graph(
            host="127.0.0.1",
            http_port=7474,
            user="neo4j",
            password="neo4j")
        self.num_limit = 20

    '''执行cypher查询，并返回相应结果'''

    def search_main(self, question, entity, risk, lat, lon):
        final_answer = ""
        # answers = []
        # enti = '.*'.join([e + '.*|' for e in entity])
        # print(enti)
        if ("地址" or "怎么走") in question:
            sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi MATCH (m:places) where m.name = '{2}' or m.name =~ '.*{2}.*' or m.name=~'.*{2}' or m.name =~'{2}.*' return m.name, m.address,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 5".format(
                lat, lon, entity)
            answers = self.g.run(sql).data()

            if answers:
                for i in answers:
                    desc = i['m.address']
                    subject = i['m.name']
                    # distince = i['distince']
                    final_answer = final_answer + \
                        '{0}的地址是：{1}\n'.format(subject, desc)
            else:
                final_answer = '您的问题暂无答案，已收录……'
        elif '电话' in question:
            sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi MATCH (m:places) where m.name = '{2}' or m.name =~ '.*{2}.*' or m.name=~'.*{2}' or m.name =~'{2}.*' return m.name,m.tel,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                lat, lon, entity)
            answers = self.g.run(sql).data()
            if answers:
                for i in answers:
                    desc = i['m.tel']
                    subject = i['m.name']
                    if '[]' in desc:
                        final_answer = final_answer + \
                            '{0}的电话暂未收录\n'.format(subject)
                    else:
                        final_answer = final_answer + \
                            '{0}的联系电话是：{1}\n'.format(subject, desc)
            else:
                final_answer = '您的问题暂无答案，已收录……'
        elif '防控措施' in question:
            if risk == 0:
                sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi match(n:places)-[r]->(m)-[t]->(p:low_measures) where n.name = '{2}' or n.name =~ '.*{2}.*' or n.name=~'.*{2}' or n.name =~'{2}.*' return n.name,t.name,p.name,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                    lat, lon, entity)
            if risk == 1:
                sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi match(n:places)-[r]->(m)-[t]->(p:mid_measures) where n.name = '{2}' or n.name =~ '.*{2}.*' or n.name=~'.*{2}' or n.name =~'{2}.*' return n.name,t.name,p.name,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                    lat, lon, entity)
            if risk == 2:
                sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi match(n:places)-[r]->(m)-[t]->(p:hig_measures) where n.name = '{2}' or n.name =~ '.*{2}.*' or n.name=~'.*{2}' or n.name =~'{2}.*' return n.name,t.name,p.name,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                    lat, lon, entity)
            answers = self.g.run(sql).data()
            if answers:
                for i in answers:
                    desc = i['p.name']
                    subject = i['n.name']
                    final_answer = final_answer + \
                        '{0}的防控建议是：\n{1}\n'.format(subject, desc)
            else:
                final_answer = '您的问题暂无答案，已收录……'
        else:
          # 语义匹配

            result_df = {'attribute': ['地址', '电话', '防控措施']}
            result_df = pd.DataFrame(result_df)
            attribute_candicate_sim = [
                (k, bs.predict(question, k)[0][1]) for k in result_df['attribute'].tolist()]
            # print(attribute_candicate_sim)
            attribute_candicate_sort = sorted(
                attribute_candicate_sim, key=lambda candicate: candicate[1], reverse=True)
            # print(attribute_candicate_sort)
            answer_candicate_df = result_df[result_df["attribute"]
                                            == attribute_candicate_sort[0][0]]
            # print("********************************************************")
            # print(answer_candicate_df)
            # print(type(answer_candicate_df))
            key = answer_candicate_df['attribute'].tolist()
            # print(key)
            if '地址' in key:
                sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi MATCH (m:places) where m.name = '{2}' or m.name =~ '.*{2}.*' or m.name=~'.*{2}' or m.name =~'{2}.*' return m.name, m.address,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                    lat, lon, entity)
                answers = self.g.run(sql).data()
                # address = answer['n.name']+answer['m.address']
                # print(answers)
                if answers:
                    for i in answers:
                        desc = i['m.address']
                        subject = i['m.name']
                        final_answer = final_answer + \
                            '{0}的地址是：{1}\n'.format(subject, desc)
                else:
                    final_answer = '您的问题暂无答案，已收录……'
            elif '电话' in key:
                sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi MATCH (m:places) where m.name = '{2}' or m.name =~ '.*{2}.*' or m.name=~'.*{2}' or m.name =~'{2}.*' return m.name,m.tel,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                    lat, lon, entity)
                answers = self.g.run(sql).data()
                if answers:
                    for i in answers:
                        desc = i['m.tel']
                        subject = i['m.name']
                        if '[]' in desc:
                            final_answer = final_answer + \
                                '{0}的电话暂未收录\n'.format(subject)
                        else:
                            final_answer = final_answer + \
                                '{0}的联系电话是：{1}\n'.format(subject, desc)
                else:
                    final_answer = '您的问题暂无答案，已收录……'
            # print(final_answer)
            elif '防控措施' in key:
                if risk == 0:
                    sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi match(n:places)-[r]->(m)-[t]->(p:low_measures) where n.name = '{2}' or n.name =~ '.*{2}.*' or n.name=~'.*{2}' or n.name =~'{2}.*' return n.name,t.name,p.name,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                        lat, lon, entity)
                if risk == 1:
                    sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi match(n:places)-[r]->(m)-[t]->(p:mid_measures) where n.name = '{2}' or n.name =~ '.*{2}.*' or n.name=~'.*{2}' or n.name =~'{2}.*' return n.name,t.name,p.namedistance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                        lat, lon, entity)
                if risk == 2:
                    sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi match(n:places)-[r]->(m)-[t]->(p:hig_measures) where n.name = '{2}' or n.name =~ '.*{2}.*' or n.name=~'.*{2}' or n.name =~'{2}.*' return n.name,t.name,p.name,distance(point({{latitude:m.lat,longitude: m.lon}}),poi) as distince order by distince asc limit 1".format(
                        lat, lon, entity)
                answers = self.g.run(sql).data()
                if answers:
                    for i in answers:
                        desc = i['p.name']
                        subject = i['n.name']
                        final_answer = final_answer + \
                            '{0}的防控建议是：\n{1}\n'.format(subject, desc)
                else:
                    final_answer = '您的问题暂无答案，已收录……'
            # print(final_answer)
        return final_answer

    def search_single(self, lat, lon):
        # enti = '.*'.join([e + '.*|' for e in entity])
        sql = "with point({{latitude:toFloat('{0}'),longitude:toFloat('{1}')}}) as poi MATCH (m:places) return m.name order by distance(point({{latitude:m.lat,longitude: m.lon}}),poi) asc limit 10".format(
            lat, lon)
        answers = self.g.run(sql).data()
        place = []
        if answers:
            for i in answers:
                place.append(i['m.name'])
        return place


if __name__ == '__main__':
    searcher = AnswerSearcher()
