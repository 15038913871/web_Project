import logging

# 配置root 日志记录器

logging.getLogger().setLevel(logging.INFO)

# 设置日志格式化
formatter = '[%(asctime)s->%(module)s->%(funcName)s]:%(massage)s'

# 设置root 的基本配置
logging.basicConfig(format=formatter,
                    datefmt='%Y-%m-%d %H:%M:%S' )