from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QMessageBox

from common.Common import check_setting, upsert_config


class SettingPage(QDialog):

    def __init__(self):
        super(SettingPage, self).__init__()
        uic.loadUi('ui/setting.ui', self)
        self.setting_save_button.clicked.connect(self.save_setting)

    # 保存配置
    def save_setting(self):
        base_url = self.base_url_edit.text()
        is_right = check_setting(base_url)
        if is_right:
            upsert_config('base_url', base_url)
            self.accept()
        else:
            QMessageBox.critical(self, '错误', '连接失败, 请检查配置')
