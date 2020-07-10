# SafeGo

这是一个为人们在新冠疫情期间提供出行建议的网站

1. 安装anaconda并利用conda创建虚拟环境，在虚拟环境中安装依赖
```
conda env create --name google -f environment.yaml
```
2. 安装nodejs，用npm安装angular
```
npm install -g @angular/cli
```
3.在cal_risk目录下的get_key.py中加入高德开发者key
```
def get_key():
    return 'key'
```
4.在KBQA_AC目录下，对answer_search.py和build_graph.py修改neo4j的数据库和密码
5.在KBQA_Bert目录下，对answer_search.py修改neo4j的数据库和密码
6.将数据库graph.db.dump导入到本地neo4j中
a.首先关闭neo4j服务，将data/databases目录下的neo4j目录删除
b.然后执行一下命令导入数据库
```
neo4j-admin load --from=PATHFORgraph.db.dump --database=neo4j --force
```
7. 进入/django/safego/KBQA_Bert文件夹下启动bert查询程序
```
python kbqa_predict.py
```
8.在/angular/safego的目录下，启动前端
 ```
ng serve
```
9. 访问浏览器

http://localhost:4200/home

10.在/django/safego的目录下，启动服务器
```
python manage.py runserver
```
