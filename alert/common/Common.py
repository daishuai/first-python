import configparser
import os

import requests

config = configparser.ConfigParser()
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
config_dir = os.path.dirname(current_dir)
print(config_dir)
config_file_path = os.path.join(config_dir, 'config/system.ini')
print(config_file_path)
config.read(config_file_path, encoding='utf-8')
print(config.sections())
print(config.options('app'))
print(config.items('app'))


def check_setting(base_url=None):
    if base_url is None or len(base_url) == 0:
        # 读取本地配置
        base_url = get_config('base_url')
        # 校验地址是否正确
    try:
        health_check_url = base_url + '/ers-service/server/monitor/health/status'
        response = requests.get(health_check_url)
        if response.text == 'ok':
            print('校验通过')
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


# 获取配置
def get_config(key):
    return config.get('app', key)


# 新增或更新配置
def upsert_config(key, value):
    config.set('app', key, value)
    with open(config_file_path, 'w') as config_file:
        config.write(config_file)
