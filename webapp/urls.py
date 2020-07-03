"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include


from safego import views,testdb,search
# django 1.1.x之前的版本 主要使用url,需要自己手动添加正则首位限制符号
# django 2.2.x之后的版本
# path:普通路径，不需要自己手动添加正则首位限制符号，底层已经添加
# re_path:用于正则路径，需要自己手动添加正则首位限制符号
urlpatterns = [
    path('admin/', admin.site.urls), # 用于配置超级用户
    path('',views.runoob),
    path('testdb/',testdb.deletedb), #这里接的应该是view.func,执行某次转发请求
    path('safego/', include("safego.urls")),
    re_path("^index/([0-9]{4})/$",views.index),
    path('app1/',include("app1.urls")), # 每个app管理自己的url,需要在每个app的目录下自己新建一个urls.py文件

]
