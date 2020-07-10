from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf #在处理post请求的时候一定要加上
from cal_risk.cal_risk import *
from KBQA_AC.chatbot import ChatBotGraph

import logging
import socket
# 响应对象主要有三种形式：HttpResponse(),render(),redirect()
# render和redirect都是对HttpResponse的封装
# render(request,页面，字典（可选，主要传的是参数））
# redirect(页面）一般用于form表单提交，跳转到新的页面

ctx={}
handler = ChatBotGraph()
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bot_address = ('127.0.0.1', 8002)
tcp_socket.connect(bot_address)

def search_advise(request):
    global ctx
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    if parameter:
        question=parameter.get('question')
        # send question to predict_online
        tcp_socket.send(question.encode('utf-8'))
        # deleted AC: answer = handler.chat_main(question)

        # get answer from predict_online
        answer = tcp_socket.recv(1024)
        print(answer)
        print(question)
        ctx['answer']=answer
        ctx['question']=question
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")


def search_risk(request):
    global ctx
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    if parameter:
        address = parameter.get('address')
        city = parameter.get('city')
        ctx['address']=address
        ctx['city']=city
        risk = cal_risk_from_name(address, city)
        strrisk=''
        if(risk==0):
            strrisk='低风险'
        elif(risk==1):
            strrisk='中风险'
        else:
            strrisk='高风险'
        ctx['risk']=strrisk
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")

def search_simple(request):
    #处理的是用户输入的地址
    global ctx
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    print(parameter)
    if parameter:
        address = parameter.get('address')
        ctx['address']=address
        city='北京'
        risk = cal_risk_from_name(address, city)
        # answer = handler.chat_main(address+'防控建议')
        # send question to predict_online
        tcp_socket.send((address+'防控意见').encode('utf-8'))

        # get answer from predict_online
        answer = tcp_socket.recv(1024)
        ctx['answer']=answer
        strrisk = ''
        if (risk == 0):
            strrisk = '低风险'
        elif (risk == 1):
            strrisk = '中风险'
        elif (risk == 2):
            strrisk = '高风险'
        else:
            strrisk = '查询不到,请检查输入的地址！'
        ctx['risk'] = strrisk
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")

def search_detail(request):
    global ctx
    parameter_json = request.body
    parameter = json.loads(parameter_json)
    print(parameter)
    if parameter:
        lnglat = parameter.get('lnglat')
        detail_address = parameter.get('detail_address')
        ctx['detail_address'] = detail_address
        ctx['lnglat']=lnglat
        city = '北京'
        real_address=detail_address.split('市')[-1]
        print(real_address)
        risk = cal_risk_from_name(real_address, city)
        # answer = handler.chat_main(detail_address+'防控建议')
        # send question to predict_online
        tcp_socket.send((detail_address+'防控意见').encode('utf-8'))

        # get answer from predict_online
        answer = tcp_socket.recv(1024)
        ctx['answer'] = answer
        strrisk = ''
        if (risk == 0):
            strrisk = '低风险'
        elif (risk == 1):
            strrisk = '中风险'
        elif(risk==2):
            strrisk = '高风险'
        else:
            strrisk='查询不到,请检查输入的地址！'
        ctx['risk'] = strrisk
    return HttpResponse(json.dumps(ctx), content_type="application/json,charset=utf-8")