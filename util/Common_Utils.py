import socket

# 超时时间, 单位秒
TIMEOUT = 5
NORMAL = 0
ERROR = 1


# 测试端口是否可用
def ping(ip, port, timeout=TIMEOUT):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (str(ip), int(port))
        status = cs.connect_ex(address)
        cs.settimeout(timeout)
        print(status)
        if status != NORMAL:
            return ERROR
        else:
            return NORMAL
    except Exception as e:
        print('error: %s' % e)
        return ERROR


# CRC16校验算法
def crc16_modbus(x, invert):
    data = bytearray.fromhex(x)
    print(data)
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for i in range(8):
            if (crc & 1) != 0:
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return hex(((crc & 0xff) << 8) + (crc >> 8))


print(ping('localhost', 15000))
print(crc16_modbus('010600010001', False))
