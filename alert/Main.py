import sys

from PyQt5.QtWidgets import QApplication, QDialog

from common.Common import check_setting
from page.MainPage import MainPage
from page.SettingPage import SettingPage


def show_main(app):
    main_window = MainPage()
    main_window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    # 创建应用
    application = QApplication(sys.argv)
    # 设置登录窗口
    login_ui = SettingPage()
    is_right = check_setting()
    if is_right:
        show_main(application)
    else:
        # 校验是否通过
        if login_ui.exec_() == QDialog.Accepted:
            show_main(application)
