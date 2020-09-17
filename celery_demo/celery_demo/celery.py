# celery.py
from celery import Celery
from django.conf import settings
import os

# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_demo.settings')

# 创建应用
app = Celery("celery_demo")

# 配置应用
app.conf.update(
    # 配置broker, 这里我们用redis作为broker
    BROKER_URL='redis://127.0.0.1:6379/8',
    # 使用项目数据库存储任务执行结果
    CELERY_RESULT_BACKEND='django-db',
    # 配置定时器模块，定时器信息存储在数据库中
    CELERYBEAT_SCHEDULER='django_celery_beat.schedulers.DatabaseScheduler',
)

# 设置app自动加载任务
# 从已经安装的app中查找任务
app.autodiscover_tasks(settings.INSTALLED_APPS)
