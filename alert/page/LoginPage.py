import json

import requests as requests
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QDialog


class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        uic.loadUi('ui/login.ui', self)
        self.login_button.clicked.connect(self.login)
        self.min_button.clicked.connect(self.min_clicked)
        self.close_button.clicked.connect(self.close_clicked)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def max_clicked(self):
        print('Maximized Window!')
        self.showMaximized()

    def min_clicked(self):
        print('Minimized Window!')
        self.showMinimized()

    def close_clicked(self):
        print('Close Window!')
        self.close()

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()
        print(f'username: {username}, password: {password}')
        if len(username) == 0 or len(password) == 0:
            QMessageBox.critical(self, '错误', '用户名或密码不能为空')
            return
        data = {'username': username, 'password': password}
        response = requests.post(url='https://iacs-dev.devdolphin.com/ers-service/oauth2/password', data=data)
        print(response.text)
        response_json = json.loads(response.text)
        if response_json['code'] != '0' or response_json['status'] != 200:
            QMessageBox.critical(self, '错误', response_json['message'])
            return
        self.accept()
