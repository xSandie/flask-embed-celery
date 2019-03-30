# flask-embed-celery
这是一个 Demo，介绍一种在 Flask 中型程序结构中使用 Celery 的方式。

欢迎大家测试、提出意见。
## 环境准备/Preparation

### 推荐版本：
- Python 3.6+；
- Flask 1.0.2；
- Celery 4.2.0；
- redis 3.2+
- rabbitmq(可不使用，直接使用redis作为消息队列)

### 环境搭建：
进入项目根目录，安装依赖
```angular2html
pip install -r requirements.txt
```

## 启动项目/Exploration：
1. 进入项目根目录，运行flask
    ```angular2html
    flask run
    ```
0. 运行Celery：
- windows  
    ```angular2html
    celery worker -A api.EmbedCelery.tasks -l info -P eventlet
    ```
- linux  
定位worker是定位到tasks里即可（api.EmbedCelery.tasks）  

**发布时记得将输出重定向到log文件中。**

## 测试/Testing
访问 http://localhost:5000
```angular2html
[tasks]
  . api.EmbedCelery.tasks.add_task
  . api.EmbedCelery.tasks.factorial_task

[2019-03-30 10:49:51,065: INFO/MainProcess] Connected to amqp://guest:**@127.0.0.1:5672//
[2019-03-30 10:49:51,094: INFO/MainProcess] mingle: searching for neighbors
[2019-03-30 10:49:52,175: INFO/MainProcess] mingle: all alone
[2019-03-30 10:49:52,207: INFO/MainProcess] celery@DESKTOP-EHBU4SK ready.
[2019-03-30 10:49:52,219: INFO/MainProcess] pidbox: Connected to amqp://guest:**@127.0.0.1:5672//.

```

## 说明/Explanation
### 诉求
- 能在 Celery 任务中使用 current_app 上下文。
- 能使用app的配置来配置celery。
- 在有蓝图的视图函数中使用celery。
### 实现
- Celery 的任务要在 Flask 的上下文中执行，因此要重写 celeryapp.Task 类。[flask官方给出了示例](http://flask.pocoo.org/docs/1.0/patterns/celery/)。
### 集成步骤
1. 将要集成进flask的celery对象整成包，tasks.py中写入需要被消费的task们，当然也可以分成不同的task模块，最后在init中导入即可。
0. 在视图函数中导入tasks中的task，导入时记得在函数内部导入，以免模块加载时使用尚等待初始化的app。










