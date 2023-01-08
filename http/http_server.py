import json
import logging

import uvicorn
from apscheduler.executors.pool import ProcessPoolExecutor
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from stomp_ws.client import Client

LOG_FORMAT = "%(asctime)s = %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

# 创建api对象
app = FastAPI()

# 挂载静态文件, 指定目录
app.mount('/static', StaticFiles(directory='static'), name='static')

# 模板目录
templates = Jinja2Templates(directory='templates')

scheduler = None


# 根路由
@app.get('/')
def root():
    return {'code': 0, 'status': 200, 'message': 'success'}


@app.get('/data/{data}')
async def read_data(request: Request, data: str):
    return templates.TemplateResponse('index.html', {'request': request, 'data': data})


@app.on_event('startup')
async def websocket_connect():
    client = Client("ws://iacs-dev.devdolphin.com/ers-service/ws/stomp/2181/9y22jdhv/websocket")
    headers = {
        'clientId': '123456789',
        'userId': 'Jack Ma',
        'onDisconnectTopic': '/disconnectTopic'
    }
    client.connect(headers=headers)
    client.subscribe(destination='/user/queue/VOICE_BROADCAST_TIPS/systemConfigByCode/pong', callback=on_receive)
    executors = {
        'default': {'type': 'threadpool', 'max_workers': 5},  # 最大工作线程数5
        'processpool': ProcessPoolExecutor(max_workers=2)  # 最大工作进程数为2
    }
    global scheduler
    scheduler = AsyncIOScheduler()
    scheduler.configure(executors=executors)
    # 添加心跳任务
    scheduler.add_job(client.heartbeat, 'interval', seconds=5)
    print("启动调度器...")
    scheduler.start()


def on_receive(frame):
    print('command: ' + frame.command)
    print('headers: ' + json.dumps(frame.headers))
    print('body: ' + json.dumps(frame.body))


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8989)
