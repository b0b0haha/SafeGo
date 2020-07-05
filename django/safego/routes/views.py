from django.shortcuts import render
from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import auth
from rest_framework.views import APIView

import json
import time,datetime
import hashlib

class risk_index(APIView):
    def post(self, request):
        parameter_json = request.body
        parameter = json.loads(parameter_json)

        get_address = 'address'
        get_city = 'city'
        get_body = 'body'
        #这个是初始化一个公共类，后面无效参数都调用这里的一个无效参数的字典，然后再转json，返回给客户端
        # 如果定义的get_phone和get_password都在请求的json中忘下走
        if get_address in parameter and get_city in parameter and get_body in parameter:
            #取出其request.json中的body和city
            address = parameter[get_address]
            city = parameter[get_city]
            body = parameter[get_body]
            # 如果phone和password都不为空
            if address and body:
                if(True):
                    datas = {
                        'status': 'true',
                        'message': '查询结果！',
                    }
                    # 字典转json返回给客户端
                    return HttpResponse(json.dumps(datas), content_type="application/json,charset=utf-8")
                else:
                    datas = {
                        'status': 'false',
                        'message': '地址为空！',
                        'data': 'null'
                    }
                return HttpResponse(json.dumps(datas), content_type="application/json,charset=utf-8")
            else:
                return HttpResponse(content_type="application/json,charset=utf-8")
        else:
            return HttpResponse(content_type="application/json,charset=utf-8")

    def json_Response(self,dict_va):
        respone_bodys=json.dumps(dict_va)
        return respone_bodys
