# 蓝牙设备地址和端口号
import bluetooth

target_address = "B8:14:4D:91:4E:D8"

device = bluetooth.find_service(address=target_address)
port = 1

# 连接蓝牙设备
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))

# 发送数据
data = "Hello, Bluetooth!"
sock.send(data)

# 接收数据
received_data = sock.recv(1024)
print("接收到的数据：", received_data)

# 关闭连接
sock.close()
