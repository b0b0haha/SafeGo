#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

from KBQA_AC.question_classifier import *
from KBQA_AC.question_parser import *
from KBQA_AC.answer_search import *

'''问答类'''


class ChatBotGraph:
    def __init__(self):
        # 问题分类
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是SafeGo，希望可以帮到您。如果没答上来，可联系https://github.com/Estherbdf/SafeGo。'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        args = res_classify['args']
        entity_dict = self.parser.build_entitydict(args)
        entities = entity_dict.get('places')
        # 计算risk
        print(entities)
        risk = 0
        res_sql = self.parser.parser_main(res_classify, risk)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        # 获取risk
        # risk = 0
        answer = handler.chat_main(question)
        print('小易:', answer)
