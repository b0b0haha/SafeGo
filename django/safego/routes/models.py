from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

class Question(models.Model):
    address =models.TextField(blank=False, null=False)
    city =models.TextField(blank=True, null=True)
    body = models.TextField(blank=False, null=False)

class Test(models.Model):
    name=models.CharField(max_length=20)
