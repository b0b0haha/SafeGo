#!/usr/bin/env python3
# coding: utf-8
# File: build_graph.py
# Author: Suriel
# Date: 20-6-24

import os
import ahocorasick
'''
    ahocosick：自动机的意思
    可实现自动批量匹配字符串的作用，即可一次返回该条字符串中命中的所有特征词
    一个句子中同时匹配字典中所有的特征词 “产褥中暑的症状和原因”
'''


class QuestionClassifier:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        #　特征词路径
        # 节点字典
        self.places_path = os.path.join(cur_dir, 'KBQA_AC/dict/places.txt')
        self.areas_path = os.path.join(cur_dir, 'KBQA_AC/dict/areas.txt')
        self.types_path = os.path.join(cur_dir, 'KBQA_AC/dict/types.txt')
        self.measures_path = os.path.join(cur_dir, 'KBQA_AC/dict/measures.txt')

        # 否定词字典
        # self.deny_path = os.path.join(cur_dir, 'dict/deny.txt')
        # 加载特征词
        self.places_wds = [i.strip() for i in open(
            self.places_path, encoding='utf-8') if i.strip()]
        self.areas_wds = [i.strip() for i in open(
            self.areas_path, encoding='utf-8') if i.strip()]
        self.types_wds = [i.strip() for i in open(
            self.types_path, encoding='utf-8') if i.strip()]
        self.measures_wds = [i.strip() for i in open(
            self.measures_path, encoding='utf-8') if i.strip()]

        # 本领域字典
        self.region_words = set(self.places_wds + self.areas_wds + self.types_wds +
                                self.measures_wds)

        # self.deny_words = [i.strip() for i in open(
        #     self.deny_path, encoding='utf-8') if i.strip()]
        # 构造领域actree
        self.region_tree = self.build_actree(list(self.region_words))
        # 构建词典
        self.wdtype_dict = self.build_wdtype_dict()
        # 问句疑问词
        self.address_qwds = ['地址', '怎么走', '在哪里', '怎么去', '在哪条街上', '在什么路上']

        self.measures_qwds = ['建议', '防控措施', '防控', '如何保护', '防止传染', '防止感染', '预防']

        self.tel_qwds = ['电话', '联系电话', '联系方式', '怎么联系', '通讯方式']
        print('model init finished ......')

        return

    '''分类主函数'''

    def classify(self, question):
        data = {}
        place_dict = self.check_place(question)
        if not place_dict:
            return {}
        # 主体
        data['args'] = place_dict
        # 收集问句当中所涉及到的实体类型
        types = []
        for type_ in place_dict.values():
            types += type_
        question_type = 'others'
        # print("***********************types*****************")
        # print(types)

        question_types = []

        # 症状
        if self.check_words(self.address_qwds, question) and ('places' in types):
            question_type = 'address'
            question_types.append(question_type)

        if self.check_words(self.tel_qwds, question) and ('places' in types):
            question_type = 'tel'
            question_types.append(question_type)

        # 原因
        if self.check_words(self.measures_qwds, question) and ('places' in types):
            question_type = 'measures'
            question_types.append(question_type)

        # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        if question_types == [] and 'places' in types:
            question_types = ['places_info']

        # # 若没有查到相关的外部查询信息，那么则将该疾病的描述信息返回
        # if question_types == [] and 'measures' in types:
        #     question_types = ['measures_info']

        # 关系，将多个分类结果进行合并处理，组装成一个字典
        data['question_types'] = question_types

        # print("---------------------question_type--------------")
        # print(data)
        return data

    '''构造词对应的类型'''

    def build_wdtype_dict(self):
        wd_dict = dict()
        for wd in self.region_words:
            wd_dict[wd] = []
            if wd in self.places_wds:
                wd_dict[wd].append('places')
            if wd in self.areas_wds:
                wd_dict[wd].append('areas')
            if wd in self.types_wds:
                wd_dict[wd].append('types')
            if wd in self.measures_wds:
                wd_dict[wd].append('measures')
        return wd_dict

    '''构造actree，用于问句中特征词匹配，加速过滤'''

    def build_actree(self, wordlist):
        actree = ahocorasick.Automaton()
        for index, word in enumerate(wordlist):
            actree.add_word(word, (index, word))
        actree.make_automaton()
        return actree

    '''问句过滤，特征词抽取'''

    def check_place(self, question):
        region_wds = []
        for i in self.region_tree.iter(question):
            wd = i[1][1]
            region_wds.append(wd)
        stop_wds = []
        for wd1 in region_wds:
            for wd2 in region_wds:
                if wd1 in wd2 and wd1 != wd2:
                    stop_wds.append(wd1)
        final_wds = [i for i in region_wds if i not in stop_wds]
        final_dict = {i: self.wdtype_dict.get(i) for i in final_wds}

        # print("----------------------final_dict----------------")
        # print(final_dict)
        return final_dict

    '''基于特征词进行分类'''

    def check_words(self, wds, sent):
        for wd in wds:
            if wd in sent:
                return True
        return False


if __name__ == '__main__':
    handler = QuestionClassifier()
    while 1:
        question = input('input an question:')
        data = handler.classify(question)
        print(data)
