import logging

import serial
from modbus_tk import modbus_rtu, modbus_tcp
import modbus_tk.defines as cst


def get_multi_open_data(channels):
    open_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for channel in channels:
        if isinstance(channel, int):
            open_data[channel - 1] = 1
        else:
            open_data[int(channel) - 1] = 1
    return open_data


def get_multi_close_data():
    close_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return close_data


class ModbusClient:

    def __init__(self, rtu_port='com3', tcp_port=502, host='127.0.0.1', baud_rate=9600, bytesize=8, parity='N',
                 stop_bits=1, client_type='rtu'):
        self.parity = parity
        self.rtu_port = rtu_port
        self.tcp_port = tcp_port
        self.host = host
        self.baud_rate = baud_rate
        self.bytesize = bytesize
        self.stop_bits = stop_bits
        self.master = None
        self.client_type = client_type

    def open_master(self):
        try:
            if self.client_type == 'rtu':
                rtu_serial = serial.Serial(port=self.rtu_port, baudrate=self.baud_rate, bytesize=self.bytesize,
                                           parity=self.parity,
                                           stopbits=self.stop_bits)
                self.master = modbus_rtu.RtuMaster(rtu_serial)
            else:
                self.master = modbus_tcp.TcpMaster(host=self.host, port=self.tcp_port)
            self.master.set_timeout(5.0)
            self.master.set_verbose(True)
            self.master.open()
        except Exception as e:
            logging.error(e)

    def close_master(self):
        logging.info('close rtu master')
        if self.master:
            self.master.close()

    def read(self, slave, address, count):
        # slave为站点号, address为寄存器开始地址, count为读取寄存器的个数
        try:
            result = self.master.execute(slave, cst.READ_HOLDING_REGISTERS, address, count)
            logging.info(result)
        except Exception as e:
            logging.error(e)

    # 写单个寄存器
    def write_single(self, slave, address, value):
        try:
            result = self.master.execute(slave, cst.WRITE_SINGLE_REGISTER, address, output_value=value)
            logging.info(result)
        except Exception as e:
            logging.warning('写单个寄存器失败')
            logging.error(e)

    # 批量写寄存器
    def write_multiple(self, slave, address, value):
        try:
            result = self.master.execute(slave, cst.WRITE_MULTIPLE_REGISTERS, address, output_value=value)
            logging.info(result)
        except Exception as e:
            logging.warning('批量写寄存器失败')
            logging.error(e)

    # 修改参数
    def write_param(self, slave, address, value):
        try:
            self.write_single(slave, 98, 1357)
            self.write_single(slave, address, value)
            self.write_single(slave, 98, 2468)
        except Exception as e:
            logging.warning('修改参数失败')
            logging.error(e)
