import json
import traceback

import websocket

CHANNELS_WS = [
    '/user/queue/demo-socket/pong'
]


class Feed(object):

    def __init__(self, url):
        self.ws = None
        self.url = url

    def on_open(self, ws):
        print('A new WebSocketApp is opened!')
        message = []
        sub_param = {
            'op': 'subscribe',
            'args': CHANNELS_WS
        }
        sub_str = json.dumps(sub_param)
        message.append(sub_str)
        ws.send('[]')
        print('Following Channels are subscribed!')
        print(CHANNELS_WS)

    def on_data(self, ws, string, type, continue_flag):
        """
        4 argument.
        The 1st argument is this class object.
        The 2nd argument is utf-8 string which we get from the server.
        The 3rd argument is data type. ABNF.OPCODE_TEXT or ABNF.OPCODE_BINARY will be came.
        The 4th argument is continue flag. If 0, the data continue
        """
        print('On Data')

    def on_message(self, ws, message):
        """
        Callback object which is called when received data.
        2 arguments:
        @ ws: the WebSocketApp object
        @ message: utf-8 data received from the server
        """
        # 对收到的message进行解析
        print('On Message')
        print(type(message))
        # result = eval(message)

    def on_error(self, ws, error):
        """
        Callback object which is called when got an error.
        2 arguments:
        @ ws: the WebSocketApp object
        @ error: exception object
        """
        print('On Error')
        traceback.print_exc(error)

    def on_close(self, ws, close_status_code, close_msg):
        """
        Callback object which is called when the connection is closed.
        2 arguments:
        @ ws: the WebSocketApp object
        @ close_status_code
        @ close_msg
        """
        print('On Close')
        print('The connection is closed! close_status_code: %s, close_msg: %s' % close_status_code % close_msg)

    def start(self):
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == '__main__':
    # feed = Feed(url='ws://127.0.0.1:8082/ws/stomp/2181/9y22jdhv/websocket')
    # feed.start()
    Byte = {
        'LF': '\x0A',
        'NULL': '\x00'
    }
    data = 'CONNECTED\nversion:1.1\nheart-beat:15000,15000\nuser-name:123456789\n\n\u0000'
    lines = data.split(Byte['LF'])
    print(lines)
