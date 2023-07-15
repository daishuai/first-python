import time

import pywinusb.hid as hid
import serial.tools.list_ports
from bluetooth import discover_devices

# 获取串口设备列表
ports = serial.tools.list_ports.comports()

# 打印串口设备信息
for port in ports:
    print(f'设备名称: {port.device}, 描述: {port.description}, 串口号: {port.serial_number}')

# 获取USB设备
devices = hid.HidDeviceFilter().get_devices()
# 打印USB设备信息
for device in devices:
    print(f'设备路径: {device.device_path}, 设备制造商: {device.vendor_name}, 设备产品: {device.product_name}')

# 列表，用于存放已搜索过的蓝牙名称
alreadyFound = []


# 搜索蓝牙
def find_devs():
    found_devs = discover_devices(lookup_names=True)
    # 循环遍历,如果在列表中存在的就不打印
    for (addr, name) in found_devs:
        if addr not in alreadyFound:
            print("[*]蓝牙设备:" + str(name))
            print("[+]蓝牙MAC:" + str(addr))
            # 新增的设备mac地址定到列表中,用于循环搜索时过滤已打印的设备
            alreadyFound.append(addr)


# 循环执行,每5秒执行一次
while True:
    find_devs()
    time.sleep(5)
