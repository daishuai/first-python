import json
import logging
import time

from stomp_ws.client import Client

LOG_FORMAT = "%(asctime)s = %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)

client = Client("ws://127.0.0.1:8082/ws/stomp/2181/9y22jdhv/websocket")
headers = {
    'clientId': '123456789',
    'userId': 'Jack Ma',
    'onDisconnectTopic': '/disconnectTopic'
}
client.connect(headers=headers)
client.subscribe('/user/queue/demo-socket/pong')
data = {
    'clientId': '1234',
    'userId': 'abcd',
    'destination': 'destination',
    'payload': 'ahla'
}
client.send('/personalData/ping', body=json.dumps(data))
time.sleep(1222)
