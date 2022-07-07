import json
import re
import time

import requests


def get_data(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    # print(response.text)
    return response.text


dic_url = 'http://i.tq121.com.cn/j/data_alarm.js'
dic_str= get_data(dic_url)
alarm_grade_str = re.search(r'gradeObj=({.*?})', dic_str).group(1)
alarm_grade_json = json.loads(alarm_grade_str)
alarm_grade_json['05'] = '未知'
print(alarm_grade_json)
alarm_kind_str = re.search(r'kindObj=({.*})', dic_str).group(1)
alarm_kind_str = re.sub('",', '","', alarm_kind_str)
alarm_kind_str = re.sub(':"', '":"', alarm_kind_str)
alarm_kind_str = re.sub('""', '"', alarm_kind_str)
alarm_kind_json = json.loads(alarm_kind_str)
print(alarm_kind_json)

timestamp = int(round(time.time() * 1000))
url = 'http://product.weather.com.cn/alarm/grepalarm_cn.php?_={}'.format(timestamp)
data_str = get_data(url)
data_json = json.loads(re.search(r'({.*})', data_str).group())
count = data_json['count']
data = data_json['data']
detail_url = 'http://www.weather.com.cn/alarm/newalarmcontent.shtml?file={}'
for d in data:
    title = d[0]
    url = d[1]
    send_time, kind, grade = re.search(r'\d*-(\d*)-(\d{2})(\d{2})', url).groups()
    print("send_time: {}, kind: {}, grade: {}".format(send_time, alarm_kind_json[kind], alarm_grade_json[grade]))
    longitude = d[2]
    latitude = d[3]
    region = d[4]
    region_ex = d[5]
    print('title: {}, url: {}, longitude: {}, latitude: {}, region: {}, region_ex: {}'
          .format(title, url, longitude, latitude, region, region_ex))
    break