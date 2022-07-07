import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def auto_code_review(username, password):
    service = Service(r'chromedriver.exe')
    browser = webdriver.Chrome(service=service)
    browser.get('http://172.16.0.124/')
    browser.find_element(value='UQ0_0').send_keys(username)  # 输入用户名
    browser.find_element(value='UQ0_1').send_keys(password)  # 输入密码
    browser.find_element(by=By.TAG_NAME, value='button').click()  # 点击登录
    browser.find_element(by=By.LINK_TEXT, value='Audit').click()  # 点击Audit
    ul_elements = browser.find_element(value='UQ0_71').find_elements(by=By.TAG_NAME, value='ul')
    li_elements = ul_elements[2].find_elements(by=By.CLASS_NAME, value='phui-oi-standard')
    cnt = len(li_elements)
    while cnt > 0:
        tapd = li_elements[0].find_element(by=By.CLASS_NAME, value='phui-oi-name').find_element(by=By.TAG_NAME,
                                                                                                value='a').text
        auditors = li_elements[0].find_element(by=By.CLASS_NAME, value='phui-oi-content').find_element(by=By.TAG_NAME,
                                                                                                       value='a').text
        print(auditors + '---' + tapd)
        # 审核人不是自己
        if auditors.count(username) == 0:
            continue
        li_elements[0].find_element(by=By.CLASS_NAME, value='phui-oi-name').find_element(by=By.TAG_NAME,
                                                                                         value='a').click()
        select_elem = browser.find_element(by=By.TAG_NAME, value='select')
        select = Select(select_elem)
        select.select_by_value('accept')
        browser.find_element(by=By.NAME, value='__submit__').click()
        time.sleep(1)
        browser.back()
        ul_elements = browser.find_element(value='UQ0_71').find_elements(by=By.TAG_NAME, value='ul')
        try:
            li_elements = ul_elements[2].find_elements(by=By.CLASS_NAME, value='phui-oi-standard')
        except IndexError:
            print('返回失败')
            browser.back()
            ul_elements = browser.find_element(value='UQ0_71').find_elements(by=By.TAG_NAME, value='ul')
            li_elements = ul_elements[2].find_elements(by=By.CLASS_NAME, value='phui-oi-standard')
        cnt = len(li_elements)
    browser.close()


auto_code_review('youliyong', 'sz123456')