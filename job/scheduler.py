import time

from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler


def heartbeat():
    print('Heartbeat!')


# 心跳任务

# 心跳任务
executors = {
    'default': {'type': 'threadpool', 'max_workers': 5},  # 最大工作线程5
    'processpool': ProcessPoolExecutor(max_workers=2)  # 最大工作进程数为2
}
scheduler = AsyncIOScheduler()
scheduler.configure(executors=executors)
scheduler.add_job(heartbeat, 'interval', seconds=5)
scheduler.start()
print('Start a job')
time.sleep(30)
