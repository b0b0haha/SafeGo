# SafeGo

这是一个为人们在新冠疫情期间提供出行建议的网站

## django设置

### 允许跨域

#### 安装corsheaders

pip install django-cors-headers

#### 配置 settings.py  

* INSTALLED_APPS添加'corsheaders'
* MIDDLEWARE 添加

```'django.middleware.common.CommonMiddleware',```

```'corsheaders.middleware.CorsMiddleware',```

* 注释

``` 
#'django.middleware.csrf CsrfViewMiddleware',
```

* 添加

```
CORS_ORIGIN_WHITELIST = (
    '127.0.0.1:8000',
    '127.0.0.1:4200',
)
```

### 运行

```
python3 ./manager.py runserver
```

## angular

### 运行

``` ng serve ```

访问http://localhost:4200