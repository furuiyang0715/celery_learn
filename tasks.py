from celery import Celery

# 我们这里案例使用redis作为broker
app = Celery('demo', broker='redis://127.0.0.1/8')


# 创建任务函数
@app.task
def my_task():
    print("任务函数正在执行.")

# 安装 redis : pip install redis

# cd 到 tasks.py 同级目录中，执行命令:
# celery -A tasks worker --loglevel=info

#  我们通过worker的控制台，可以看到我们的任务被worker处理。调用一个任务函数，将会返回一个AsyncResult对象，这个对象可以用来检查任务的状态或者获得任务的返回值。

