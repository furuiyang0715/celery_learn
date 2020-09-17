from celery import Celery
from celery.schedules import crontab

app = Celery('mypro')
app.config_from_object('mypro.celeryconfig')

# app.conf.task_default_queue = 'default'
# app.conf.task_routes = ([
#     ('mypro.tasks.my_add', {'queue': 'queue1'}),
#     ('mypro.tasks.my_sub', {'queue': 'queue1'}),
#     ('mypro.tasks.my_mul', {'queue': 'queue2'}),
#     ('mypro.tasks.*', {'queue': 'default'}),
# ],)


'''(1) 开启两个任务服务器 分别处理两个队列
celery -A mypro worker --loglevel=info -Q queue1
celery -A mypro worker --loglevel=info -Q queue2 

(2) 也可以在一个任务服务器中开启两个队列 
celery -A mypro worker --loglevel=info -Q queue1,queue2
以下与不指定具体的队列效果相同: 
celery -A mypro worker --loglevel=info -Q queue1,queue2,default

(3) 在注册任务时主动指定使用的队列: 
'''


# 增加 celery beat 的配置信息
# 启动定时任务的命令: celery -A mypro worker --loglevel=info --beat
app.conf.timezone = 'Asia/Shanghai'
app.conf.beat_schedule = {
    'every-15-seconds':
        {
            'task': 'mypro.tasks.my_add',
            'schedule': 15.0,
            'args': (16, 16),
        },

    # 'add-every-wednesday-afternoon':
    #     {
    #         'task': 'mypro.tasks.my_mul',
    #         'schedule': crontab(minute=25, hour=16, day_of_week=3),
    #         'args': (16, 16),
    #     },

}

# 自动搜索任务
app.autodiscover_tasks(['mypro'])