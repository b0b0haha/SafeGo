# SafeGo
这是一个为人们在新冠疫情期间提供出行建议的网站
## 运行说明
1.在webapp根目录下安装所需的依赖
```
pip install -r requirements.txt
```
2.在cal_risk目录下的get_key.py中加入key
```
def get_key():
    return 'key'
```
3.在KBQA_AC目录下，对answer_search.py和build_graph.py修改neo4j的数据库和密码
4.在webapp的目录下，启动服务器
```
python manage.py runserver
```
5.访问页面
http://127.0.0.1:8000/safego/search-form/
