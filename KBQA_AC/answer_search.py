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
        final_answer = []
        if not answers:
            return ''
        if question_type == 'address':
            desc = [i['m.address'] for i in answers]
            subject = answers[0]['m.name']

            final_answer = '{0}的地址是：{1}'.format(
                subject, ';'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'tel':
            desc = []
            desc = [i['m.tel'] for i in answers]
            # print(desc)
            # print(list(set(desc)))
            subject = answers[0]['m.name']
            if '[]' in desc:
                final_answer = '{0}的电话暂未收录'.format(subject)
            else:
                final_answer = '{0}的电话是：{1}'.format(
                    subject, ';'.join(list(set(desc))[:self.num_limit]))

        elif question_type == 'measures':
            desc = [i['p.name'] for i in answers]
            subject = answers[0]['n.name']
            final_answer = '{0}的防控建议是：\t{1}'.format(
                subject, ';'.join(list(set(desc))[:self.num_limit]))
        elif question_type == 'places_info':
            desct = []
            desca = [i['n.address'] for i in answers]
            desct = [i['n.tel'] for i in answers]
            descm = [i['p.name'] for i in answers]
            subject = answers[0]['n.name']
            if '[]' in desct:
                final_answer = '{0}的地址是：{1}, \n防控建议是：{2}'.format(
                    subject, ';'.join(list(set(desca))[:self.num_limit]), ';'.join(list(set(descm))[:self.num_limit]))
            else:
                final_answer = '{0}的地址是：{1}, \n联系电话是：{2}, \n防控建议是：{3}'.format(
                    subject, ';'.join(list(set(desca))[:self.num_limit]), ';'.join(list(set(desct))[:self.num_limit]), ';'.join(list(set(descm))[:self.num_limit]))

        return final_answer


if __name__ == '__main__':
    searcher = AnswerSearcher()
