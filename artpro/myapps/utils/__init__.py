# '''
# 多模块之间的工具包
# '''
import logging
import os

from redis import Redis

from MArtPro import settings

# 声明redis缓存
from MArtPro.settings import REDIS_CACHE

redis_cache = Redis(**REDIS_CACHE)

def mvImage(filePath, dstDir):
    '''
    将filePath位置的文件，移动到dstDir目录下
    :param filePath:
    :param dstDir:
    :return:
    '''
    # 读取到文件名
    tmpDir, fileName = os.path.split(filePath)

    with open(filePath, 'rb') as rf:
        with open(os.path.join(dstDir, fileName), 'wb') as wf:
            wf.write(rf.read())

    # 清空临时目录
    for tmpFileName in os.listdir(tmpDir):
        os.remove(os.path.join(tmpDir, tmpFileName))

    return fileName


# 针对ajax上传文件，且被用户注册使用后，将图片文件移动到/static/users/目录
# 同时将上传图片存储的目录的临时清空
def mvImageFromTmp(filePath):
    dstDir = os.path.join(settings.BASE_DIR, 'static/users')

    srcPath = os.path.join(settings.BASE_DIR, filePath[1:])

    return os.path.join('/static/users', mvImage(srcPath, dstDir))