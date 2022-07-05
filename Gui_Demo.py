import os
import sys
import tkinter
import time
from tkinter import filedialog

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def auto_code_review(username, password, path):
    service = Service(path)
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


def get_path(path_text):
    path = filedialog.askopenfilename(title='请选择文件')
    path_text.set(path)


window = tkinter.Tk()
window.title('代码评审')
window.geometry('500x200')
username_entry = tkinter.Entry(window, show='')
username_label = tkinter.Label(window, text='输入用户名')
username_entry.place(x=200, y=6)
username_label.place(x=120, y=6)
password_entry = tkinter.Entry(window, show='*')
password_label = tkinter.Label(window, text='输入密码')
password_entry.place(x=200, y=40)
password_label.place(x=120, y=40)
path_text = tkinter.StringVar()
path_entry = tkinter.Entry(window, textvariable=path_text)
path_label = tkinter.Label(window, text='请输入路径')
path_entry.place(x=200, y=80)
path_label.place(x=120, y=80)
file_button = tkinter.Button(window, text='选择路径', command=lambda: get_path(path_text))
exit_button = tkinter.Button(window, text='退出', command=lambda: window.destroy(), width=5, height=1)
start_button = tkinter.Button(window, text='开始',
                              command=lambda: auto_code_review(username_entry.get(), password_entry.get(), path_text.get()),
                              width=5, height=1)
file_button.place(x=350, y=75)
exit_button.place(x=250, y=120, anchor='nw')
start_button.place(x=190, y=120, anchor='nw')
window.mainloop()
