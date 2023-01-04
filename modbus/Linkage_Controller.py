from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
import serial
import logging
import serial.tools.list_ports
import numpy as np


class LinkageController(object):

    def __init__(self, port='com3', baudrate=9600, bytesize=8, parity='N', stopbits=1):
        self.master = None
        self.log = logging
        self.port = port  # 端口号
        self.baudrate = baudrate  # 波特率
        self.bytesisze = bytesize  # 数据位
        self.parity = parity  # 校验位
        self.stopbits = stopbits  # 停止位

    def rtu_master(self):
        try:
            self.master = modbus_rtu.RtuMaster(
                serial.Serial(port=self.port, baudrate=self.baudrate, bytesize=self.bytesisze, parity=self.parity,
                              stopbits=self.stopbits))
            self.master.set_timeout(1)
            self.master.set_verbose(True)
            self.master.open()
            return True
        except Exception as e:
            print(e)
            self.log.error(e)
            return False

    def rtu_read(self, slave, address, count):
        # slave为站点号, address为寄存器开始地址, count为读取寄存器的个数
        try:
            result = self.master.execute(slave, cst.READ_HOLDING_REGISTERS, address, count)
            print(result)
            self.log.info(result)
        except Exception as e:
            self.log.error(e)

    def rtu_write_single(self, slave, address, value):
        result = self.master.execute(slave, cst.WRITE_SINGLE_REGISTER, address, output_value=value)
        self.log.info(result)

    def rtu_write_multiple(self, slave, address, value):
        result = self.master.execute(slave, cst.WRITE_MULTIPLE_REGISTERS, address, output_value=value)
        self.log.info(result)


ports = list(serial.tools.list_ports.comports())
for port in ports:
    print(port)


def padded_hex(i, l):
    given_int = i
    given_len = l

    hex_result = hex(given_int)[2:]  # remove '0x' from beginning of str
    num_hex_chars = len(hex_result)
    extra_zeros = '0' * (given_len - num_hex_chars)  # may not get used..

    return ('0x' + hex_result if num_hex_chars == given_len else
            '?' * given_len if num_hex_chars > given_len else
            '0x' + extra_zeros + hex_result if num_hex_chars < given_len else
            None)


def getArr(arr):
    if not arr:
        return None
    res = {
        1: [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        2: [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        3: [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        4: [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        5: [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        6: [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        7: [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        8: [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        9: [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        10: [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        11: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        12: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        13: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        14: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        15: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        16: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    }
    c = np.array([0])
    for i, v in enumerate(arr):
        c = c + np.array(res[v])
    return c.tolist()


print(bytes.fromhex('01 06 00 00 00 00 89 CA'))
print(b'\x01\x06\x00\x00\x00\x00\x89\xca'.hex())
print(padded_hex(11, 4))
print(getArr(list(map(int, '2,3,4'.split(',')))))
'''
语法
map(function, iterrable, .....)
参数解释
func，是处理序列中每一个元素的函数
iterrable，序列，可以是一个或多个
返回值
返回迭代器
'''
print(type(map(int, '2,4,5'.split(','))))
