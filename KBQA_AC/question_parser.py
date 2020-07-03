#!/usr/bin/env python3
# coding: utf-8
# File: question_parser.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

# 根据object和relation构造查询语句
class QuestionPaser:

    '''构建实体节点'''

    def build_entitydict(self, args):
        entity_dict = {}
        for arg, types in args.items():
            for type in types:
                if type not in entity_dict:
                    entity_dict[type] = [arg]
                else:
                    entity_dict[type].append(arg)

        return entity_dict

    '''解析主函数'''

    def parser_main(self, res_classify, risks):
        # print("*********************************parser_main****************************")
        args = res_classify['args']
        entity_dict = self.build_entitydict(args)
        entities = entity_dict.get('places')
        question_types = res_classify['question_types']
        sqls = []
        for question_type in question_types:
            sql_ = {}
            sql_['question_type'] = question_type
            sql = []
            if question_type == 'address':
                # print(entity_dict.get('places'))
                sql = self.sql_transfer(
                    question_type, entities, risks)

            elif question_type == 'tel':
                sql = self.sql_transfer(
                    question_type, entities, risks)

            elif question_type == 'measures':
                sql = self.sql_transfer(
                    question_type, entities, risks)

            elif question_type == 'places_info':
                sql = self.sql_transfer(
                    question_type, entities, risks)

            if sql:
                sql_['sql'] = sql

                sqls.append(sql_)

        return sqls

    '''针对不同的问题，分开进行处理'''

    def sql_transfer(self, question_type, entities, risk):
        # print(risk)
        # print(question_type)
        if not entities:
            return []
        # 查询语句
        sql = []
        # print("*********************************sql_transfer**********************")
        # 查询地址
        if 'address' in question_type:
            sql = ["MATCH (m:places) where m.name = '{0}'return m.name, m.address".format(
                i) for i in entities]

        # 查询电话
        elif 'tel' in question_type:
            sql = ["MATCH (m:places) where m.name = '{0}'return m.name,m.tel".format(
                i) for i in entities]

        # 查询防控措施
        elif 'measures' in question_type:
            if risk == 0:
                sql = ["match(n:places)-[r]->(m)-[t]->(p:low_measures) where n.name = '{0}'return n.name,t.name,p.name".format(
                    i) for i in entities]

            if risk == 1:
                sql = ["match(n:places)-[r]->(m)-[t]->(p:mid_measures) where n.name = '{0}'return n.name,t.name,p.name".format(
                    i) for i in entities]
            if risk == 2:
                sql = ["match(n:places)-[r]->(m)-[t]->(p:hig_measures) where n.name = '{0}'return n.name,t.name,p.name".format(
                    i) for i in entities]
        elif 'places_info' in question_type:

            if risk == 0:
                sql = ["match(n:places)-[r]->(m)-[t]->(p:low_measures) where n.name = '{0}'return n.name,n.address,n.tel,p.name".format(
                    i) for i in entities]
            if risk == 1:
                sql = ["match(n:places)-[r]->(m)-[t]->(p:mid_measures) where n.name = '{0}'return n.name,n.address,n.tel,p.name".format(
                    i) for i in entities]
            if risk == 2:
                sql = ["match(n:places)-[r]->(m)-[t]->(p:hig_measures) where n.name = '{0}' return n.name,n.address,n.tel,p.name".format(
                    i) for i in entities]
            # print(sql)

        return sql


if __name__ == '__main__':
    handler = QuestionPaser()
