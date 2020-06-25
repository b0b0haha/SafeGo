from django.contrib import admin
from safego.models import Test
# Register your models here.
# 主要是方便admin界面管理数据模型，需要先注册数据模型到admin

admin.site.register(Test)