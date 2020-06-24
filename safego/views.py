from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def runoob(request):
    context= {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context) # render传了一个字典作为参数


