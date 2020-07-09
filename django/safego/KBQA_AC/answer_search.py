#!/usr/bin/env python3
# coding: utf-8
# File: build_graph.py
# Author: Suriel
# Date: 20-6-24

from py2neo import Graph


class AnswerSearcher:
    def __init__(self):
        self.g = Graph(
            host="127.0.0.1",
            http_port=7474,
            user="neo4j",
            password="neo4j")
        self.num_limit = 20

    '''执行cypher查询，并返回相应结果'''

    def search_main(self, sqls):
        final_answers = []
        for sql_ in sqls:
            question_type = sql_['question_type']
            queries = sql_['sql']
            answers = []
            for query in queries:
                ress = self.g.run(query).data()
                answers += ress
            final_answer = self.answer_prettify(question_type, answers)
            if final_answer:
                final_answers.append(final_answer)
        return final_answers

    '''根据对应的qustion_type，调用相应的回复模板'''

    def answer_prettify(self, question_type, answers):
        final_answer = ""
        if not answers:
            return ''
        if question_type == 'address':
            for i in answers:
                desc = i['m.address']
                subject = i['m.name']
                final_answer = final_answer + '{0}的地址是：{1}\n'.format(
                    subject, desc)

        elif question_type == 'tel':
            desc = []

            for i in answers:
                desc = i['m.tel']
                subject = i['m.name']
                if '[]' in desc:
                    final_answer = final_answer + \
                        '{0}的电话暂未收录\n'.format(subject)
                else:
                    final_answer = final_answer + '{0}的电话是：{1}\n'.format(
                        subject, desc)

        elif question_type == 'measures':
            for i in answers:
                desc = i['p.name']
                subject = i['n.name']
                final_answer = final_answer + '{0}的防控建议是：\n{1}\n'.format(
                    subject, desc)
        elif question_type == 'places_info':
            desct = []
            for i in answers:
                desca = i['n.address']
                desct = i['n.tel']
                descm = i['p.name']
                subject = i['n.name']
                if '[]' in desct:
                    final_answer = final_answer + '{0}的地址是：{1}, \n防控建议是：\n{2}\n'.format(
                        subject, desca, descm)
                else:
                    final_answer = final_answer + '{0}的地址是：{1}, \n联系电话是：{2}, \n防控建议是：{3}\n'.format(
                        subject, desca, desct, descm)

        return final_answer


if __name__ == '__main__':
    searcher = AnswerSearcher()
