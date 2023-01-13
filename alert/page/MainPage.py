from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class MainPage(QMainWindow):

    def __init__(self):
        super(MainPage, self).__init__()
        uic.loadUi('ui/main.ui', self)
