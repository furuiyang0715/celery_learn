from celery import Celery

app = Celery('mypro')
app.config_from_object('mypro.celeryconfig')

# 自动搜索任务
app.autodiscover_tasks(['mypro'])
