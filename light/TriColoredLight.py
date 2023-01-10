import socket


class TriColoredLight(object):

    def __init__(self, host, port=20108):
        self.port = port
        self.host = host
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'default socket timeout {self.socket_client.gettimeout()}')
        self.socket_client.settimeout(5)
        print(f'current socket timeout {self.socket_client.gettimeout()}')
        addr = (self.host, int(self.port))
        self.socket_client.connect(addr)

    def send(self, data):
        self.socket_client.send(bytes(data, 'utf-8'))


if __name__ == '__main__':
    tri_colored_light = TriColoredLight(host='192.168.110.71')
    tri_colored_light.send('BJ:1,50000,0,OK')
