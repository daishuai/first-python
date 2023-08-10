import json
import logging
import time

from stomp_ws.client import Client

LOG_FORMAT = "%(asctime)s = %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)


def on_receive(frame):
    print('command: ' + frame.command)
    print('headers: ' + json.dumps(frame.headers))
    print('body: ' + json.dumps(frame.body))


client = Client("ws://iacs-dev.devdolphin.com/ers-service/ws/stomp/2181/9y22jdhv/websocket")
headers = {
    'clientId': '123456789',
    'userId': 'Jack Ma',
    'onDisconnectTopic': '/disconnectTopic'
}
client.connect(headers=headers)
primary_key, unsubscribe = client.subscribe(destination='/user/queue/demo-socket/pong', callback=on_receive)
print(f'id: {primary_key}')
print(type(unsubscribe))
unsubscribe()
data = {
    'clientId': '1234',
    'userId': 'abcd',
    'destination': 'destination',
    'payload': 'ahla'
}
client.send('/personalData/ping', body=json.dumps(data))
time.sleep(1500)
print('结束')
