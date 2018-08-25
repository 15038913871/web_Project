# 声明celery 对象
from __future__ import absolute_import
import os

import django
from celery import Celery

#设置环境变量 DJANGO_SETTINGS_MODULE
from MArtPro import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','MArtPro.settings')

app = Celery('sunny')#创建celery应用


# 配置Celery 应用对象
app.config_from_object('django.conf:settings')

# 自动查找当前项目中的Celery 的Task(异步函数)
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)
