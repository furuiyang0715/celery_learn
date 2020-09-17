from celery import Celery

# # (1) 在初始化 app 的时候进行配置
# app = Celery('demo',
#              backend='redis://127.0.0.1:6379/8',
#              broker='redis://127.0.0.1:6379/9')


# # （2） 通过 app 的 conf 属性进行配置
# app = Celery('demo')
# app.conf.update(
#     result_backend='redis://127.0.0.1:6379/8',
#     broker_url='redis://127.0.0.1:6379/9',
# )


# (3) 通过专用的配置文件来加载配置
app = Celery('demo')
'''
下面我们在tasks.py模块 同级目录下创建配置模块celeryconfig.py:
result_backend = 'redis://127.0.0.1:6379/8'
broker_url = 'redis://127.0.0.1:6379/9'
'''
app.config_from_object('celeryconfig')


@app.task
def my_task(a, b):
    print("任务函数正在执行.")
    return a + b


'''
更多配置: http://docs.celeryproject.org/en/latest/userguide/configuration.html#configuration 

'''