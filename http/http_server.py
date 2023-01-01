import uvicorn
from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

# 创建api对象
app = FastAPI()

# 挂载静态文件, 指定目录
app.mount('/static', StaticFiles(directory='static'), name='static')

# 模板目录
templates = Jinja2Templates(directory='templates')


# 根路由
@app.get('/')
def root():
    return {'code': 0, 'status': 200, 'message': 'success'}


@app.get('/data/{data}')
async def read_data(request: Request, data: str):
    return templates.TemplateResponse('index.html', {'request': request, 'data': data})


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8989)
