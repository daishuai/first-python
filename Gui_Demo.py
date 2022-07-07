import os
import sys
import tkinter
import time
from tkinter import filedialog

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def auto_code_review(username, password, ul_index=2):
    base_path = os.path.dirname(os.path.realpath(sys.executable))
    path = os.path.join(base_path, 'chromedriver.exe')
    service = Service(path)
    browser = webdriver.Chrome(service=service)
    browser.get('http://172.16.0.124/')
    browser.find_element(value='UQ0_0').send_keys(username)  # 输入用户名
    browser.find_element(value='UQ0_1').send_keys(password)  # 输入密码
    browser.find_element(by=By.TAG_NAME, value='button').click()  # 点击登录
    browser.find_element(by=By.LINK_TEXT, value='Audit').click()  # 点击Audit
    ul_elements = browser.find_element(value='UQ0_71').find_elements(by=By.TAG_NAME, value='ul')
    li_elements = ul_elements[ul_index].find_elements(by=By.CLASS_NAME, value='phui-oi-standard')
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
            li_elements = ul_elements[ul_index].find_elements(by=By.CLASS_NAME, value='phui-oi-standard')
        except IndexError:
            print('返回失败')
            browser.back()
            ul_elements = browser.find_element(value='UQ0_71').find_elements(by=By.TAG_NAME, value='ul')
            li_elements = ul_elements[ul_index].find_elements(by=By.CLASS_NAME, value='phui-oi-standard')
        cnt = len(li_elements)
    browser.close()


window = tkinter.Tk()
window.title('代码评审')
window.geometry('300x200')
username_entry = tkinter.Entry(window, show='')
username_label = tkinter.Label(window, text='输入用户名')
username_entry.place(x=110, y=16)
username_label.place(x=40, y=16)
password_entry = tkinter.Entry(window, show='*')
password_label = tkinter.Label(window, text='输入密码')
password_entry.place(x=110, y=50)
password_label.place(x=40, y=50)
exit_button = tkinter.Button(window, text='退出', command=lambda: window.destroy(), width=5, height=1)
start_button = tkinter.Button(window, text='开始',
                              command=lambda: auto_code_review(username_entry.get(), password_entry.get()),
                              width=5, height=1)
start_button.place(x=90, y=90, anchor='nw')
exit_button.place(x=190, y=90, anchor='nw')
window.mainloop()
