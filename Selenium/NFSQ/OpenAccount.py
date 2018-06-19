# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 上午10:57
# @Author  : Jane
# @Site    : 
# @File    : OpenAccount.py
# @Software: PyCharm

from selenium import webdriver
import time


def login(driver):

    url = 'http://ibpm-dev.yst.com.cn:8808/Logon.aspx'
    driver.get(url)
    uname = driver.find_element_by_id('txtUserName').send_keys('xlli45')
    passwd = driver.find_element_by_id('txtPassword').send_keys('admin@123')
    driver.find_element_by_id('btnLogin').click()
    return 'login success'

def changUser(driver):
    time.sleep(2)
    # 无法获取弹出框的内容
    driver.find_element_by_class_name('hidden-xs').click()
    driver.find_element_by_xpath('//*[@id="txtSearch"]').send_keys("刘银行")
    driver.find_element_by_id('btnSearch').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="datagrid-row-r1-2-0"]/td[1]/div/input').click()
    return 'change user'


if __name__ == '__main__':
    driver = webdriver.Chrome()
    #流程登录
    loginInfo = login(driver)
    time.sleep(3)
    #切换用户
    changeInfo = changUser(driver)

    url = 'http://ibpm-dev.yst.com.cn:8808/StepPages/TaskPage.aspx?P=%E9%87%8F%E8%B4%A9%E8%87%AA%E8%B4%A9%E6%9C%BA%E7%BB%8F%E9%94%80%E5%95%86%E5%BC%80%E6%88%B7%E7%94%B3%E8%AF%B7&TaskID=S041316333640719117e4ce4079e5ef&t=1805221058'
    driver.get(url)
    # 经销商基本信息
    driver.find_element_by_id('BASIC_SFXYGSJXS_0').click()
    driver.find_element_by_xpath('//*[@id="li_BASIC_JXSDM"]/div/span/input[1]').send_keys('0000100039')
    driver.find_element_by_xpath('//*[@id="li_BASIC_HZLX"]/div/span/input[1]').send_keys('量贩自贩机经销商')
    driver.find_element_by_xpath('//*[@id="BASIC_FZR"]').send_keys('1111')
    driver.find_element_by_xpath('').send_keys('')
    driver.find_element_by_xpath('').send_keys('')

    print(message)
