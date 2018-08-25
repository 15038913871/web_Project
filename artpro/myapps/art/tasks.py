import time
from utils import red
from MArtPro.celery import app

@app.task
def advanceArt(artId,userId):
    # 抢读（artId 文章id,userId 当前用户登录）id
    print("用户",userId,"正在抢读",artId)
    time.sleep(10)
    return artId + "抢读成功"

@app.task
def sendEmailLog():
    # 读取指定日志文件的内容，并发送给管理员
    time.sleep(5)
    print("已发送邮箱")
    return "日志邮箱已发送"