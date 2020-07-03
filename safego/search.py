from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators import csrf #在处理post请求的时候一定要加上
from cal_risk.cal_risk import *
from KBQA_AC.chatbot import ChatBotGraph
# 响应对象主要有三种形式：HttpResponse(),render(),redirect()
# render和redirect都是对HttpResponse的封装
# render(request,页面，字典（可选，主要传的是参数））
# redirect(页面）一般用于form表单提交，跳转到新的页面

ctx={}
handler = ChatBotGraph()

# 表单
def search_form(request):
    return render(request,'search_form.html',context=None)


# 接收请求数据
def search_get(request):
    global ctx

    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']: #GET和POST属性都是django.http.QueryDict类的实例，这相当于dict自定义的一个类，可以单键多值

        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    ctx['rlt1']=message
    return render(request,"search_form.html",ctx)

def search_advise(request):
    global ctx
    global handler
    if request.POST:
        question=request.POST['q']
        print(question)
        answer = handler.chat_main(question)
        ctx['answer']=answer
        ctx['question']=question
    return render(request,"search_form.html",ctx)


def search_risk(request):
    global ctx
    if request.POST:
        address = request.POST.get('address')
        city = request.POST.get('city')
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
        print(address,city,risk)
    return render(request, "search_form.html", ctx)








