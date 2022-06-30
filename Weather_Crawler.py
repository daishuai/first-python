from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'C:\Software\Python\Python310\Lib\site-packages\selenium\webdriver\chrome\chromedriver.exe')
browser = webdriver.Chrome(service=service)
browser.get('http://www.weather.com.cn/alarm/alarm_list.shtml')
iframe = browser.find_element(by=By.TAG_NAME, value='iframe')
browser.switch_to.frame(iframe)
ul_elements = browser.find_element(by=By.CLASS_NAME, value='dDisasterAlarm').find_elements(by=By.TAG_NAME, value='ul')
print('ul_elements size: {}'.format(len(ul_elements)))
for ul_element in ul_elements:
    li_elements = ul_element.find_elements(by=By.TAG_NAME, value='li')
    for li_element in li_elements:
        num = li_element.find_element(by=By.CLASS_NAME, value='shuzi').text
        content = li_element.find_elements(by=By.TAG_NAME, value='a')[1].text
        date = li_element.find_element(by=By.CLASS_NAME, value='dTime').text
        print('序号: {}, 内容: {}, 发布时间: {}'.format(num, content, date))
    browser.find_element(by=By.CLASS_NAME, value='nextpage').click()
browser.close()
