from django.shortcuts import render ,redirect #可以重定向页面，将请求的页面返回
#from django.views.decorators import csrf #在处理post请求的时候一定要加上
# Create your views here.
from django.http import HttpResponse # 直接返回数据的方式
from django.urls import reverse

def runoob(request):
    context= {}
    context['hello'] = 'Hello World!'
    context['name']='菜鸟教程'
    return render(request, 'runoob.html', context) # render传了一个字典作为参数

def index(request,m): # 对应到url中
    print(m) #一个形参代表路径中的一个分组的内容，按照顺序进行匹配
    return HttpResponse('菜鸟教程')
def login1(request):
    return render(request,'login.html')

def answer(request):
    return render(request, 'QA.html')

def login(request,args):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        if username=="菜鸟教程" and pwd=="1234":
            return HttpResponse("菜鸟教程")
        else:
            return redirect(reverse('login',args=(10,)))
