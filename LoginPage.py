import sys

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget


class LoginPage(QWidget):
    def __init__(self):
        super(LoginPage, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.login_button.clicked.connect(self.login_in)
        self.min_button.clicked.connect(self.min_clicked)
        self.close_button.clicked.connect(self.close_clicked)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def login_in(self):
        print('Hello World!')
        pass

    def max_clicked(self):
        print('Maximized Window!')
        self.showMaximized()

    def min_clicked(self):
        print('Minimized Window!')
        self.showMinimized()

    def close_clicked(self):
        print('Close Window!')
        self.close()


def show_login():
    app = QtWidgets.QApplication(sys.argv)
    login_page = LoginPage()
    login_page.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    show_login()
