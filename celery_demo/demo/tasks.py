from celery_demo.celery import app
import time


# 加上app对象的task装饰器
# 此函数为任务函数
@app.task
def my_task():
    print("任务开始执行....")
    time.sleep(1)
    print("任务执行结束....")
    return '我是任务执行的结果'


@app.task
def interval_task():
    print("我每隔5秒钟时间执行一次....")
    return int(time.time() * 1000)
