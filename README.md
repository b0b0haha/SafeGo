# SafeGo
这是一个为人们在新冠疫情期间提供出行建议的网站
## 环境需要
neo4j-4.1.0， python3.x
## 运行说明
1.在webapp根目录下安装所需的依赖
```
pip install -r requirements.txt
```
2.在cal_risk目录下的get_key.py中加入高德开发者key
```
def get_key():
    return 'key'
```
3.在KBQA_AC目录下，对answer_search.py和build_graph.py修改neo4j的数据库和密码
4.将数据库graph.db.dump导入到本地neo4j中
a.首先关闭neo4j服务，将data/databases目录下的neo4j目录删除
b.然后执行一下命令导入数据库
```
neo4j-admin load --from=PATHFORgraph.db.dump --database=neo4j --force
```
4.在SafeGo的目录下，启动服务器
```
python manage.py runserver
```
5.访问页面
http://127.0.0.1:8000/safego/search-form/
