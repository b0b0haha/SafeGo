from django.shortcuts import render #可以重定向页面，将请求的页面返回

# Create your views here.
from django.http import HttpResponse # 直接返回数据的方式
def runoob(request):
    context= {}
    context['hello'] = 'Hello World!'
    context['name']='菜鸟教程'
    return render(request, 'runoob.html', context) # render传了一个字典作为参数

def index(request,year):
    print(year) #一个形参代表路径中的一个分组的内容，按照顺序进行匹配
    return HttpResponse('菜鸟教程')


