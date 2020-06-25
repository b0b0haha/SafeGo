from django.db import models

# Create your models here.
# 这里每个class都是一个表，在每个class里面可以定义属性列
class Test(models.Model):
    name=models.CharField(max_length=20)