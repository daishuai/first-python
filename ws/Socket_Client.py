import socketio


def create_client():
    sio = socketio.Client()

    @sio.event
    def connect():
        print('connection established')

    # 监听服务端推送消息
    @sio.event
    def user_message(data):
        print('user_message received with', data)

    @sio.event
    def disconnect():
        print('disconnected from server')

    # 连接服务端
    sio.connect('http://localhost:5000')
    print('000')
    sio.wait()


create_client()
