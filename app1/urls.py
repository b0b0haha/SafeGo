from django.contrib import admin
from django.urls import path,re_path,include
from app1 import views
urlpatterns=[
   path('login1/',views.login1),
   re_path(r"^login/([0-9]{2})/$", views.login, name="login"),
   #re_path(r'^login/(?P<m>[0-9]{2})/$', views.index), #这里的m要指定在view中进行处理
   # (?P<组名>正则表达式)
]