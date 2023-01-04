import os.path
from tempfile import NamedTemporaryFile

import win32print
import win32ui
from PIL import Image

# 默认打印机的名称
printer_name = win32print.GetDefaultPrinter()
print(printer_name)
# 调用打印机打印图片
hDC = win32ui.CreateDC()
hDC.CreatePrinterDC(printer_name)

# 打开图片
bmp = Image.open("D:\\Users\\keda\\Pictures\\start\\Jay.jpg")


def get_abs_path(path: str):
    # __file__表示当前文件路径
    # os.path.dirname() 去掉文件名, 返回目录
    current_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.abspath(os.path.dirname(current_path) + "/" + path)