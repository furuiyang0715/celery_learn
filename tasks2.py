from celery import Celery

# 我们这里案例使用 redis 作为 broker
app = Celery('demo',
             backend='redis://127.0.0.1:6379/8',
             broker='redis://127.0.0.1:6379/9')


@app.task
def my_task(a, b):
    print("任务函数正在执行.")
    return a + b



'''任务说明:
如果我们想跟踪任务的状态，Celery 需要将结果保存到某个地方。有几种保存的方案可选: SQLAlchemy、Django ORM、Memcached、 Redis、RPC (RabbitMQ/AMQP).
例子我们仍然使用 Redis 作为存储结果的方案，任务结果存储配置我们通过 Celery 的 backend 参数来设定.



'''
