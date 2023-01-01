import eventlet
import socketio


def create_server():
    sio = socketio.Server()
    app = socketio.WSGIApp(sio, static_files={
        '/': {'content_type': 'text/html', 'filename': 'index.html'}
    })

    @sio.event
    def connect(sid, environ):
        print('connect', sid)
        sio.emit('serve', {'response': 'connect success'})

    if __name__ == '__main__':
        eventlet.wsgi.server(eventlet.listen(('', 5000)), app)


create_server()
