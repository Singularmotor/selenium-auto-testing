#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

def qqlo(a,b):
    wf.get("http://www.qq.com")
    wf.implicitly_wait(2)
    wf.find_element_by_xpath(".//*[@id='loginGrayLayout']").click()
    wf.switch_to_frame("login_frame")  # 进行弹出窗口操作
    time.sleep(1)
    wf.find_element_by_xpath(".//*[@id='switcher_plogin']").click()

    wf.find_element_by_id("u").clear()
    wf.find_element_by_id("u").send_keys(a)  # 账号输入
    time.sleep(1)
    wf.find_element_by_id("p").clear()
    wf.find_element_by_id("p").send_keys(b)  # 密码输入
    time.sleep(1)
    wf.find_element_by_id("login_button").click()  # 登录按钮
    time.sleep(6)



def qqlout():
    wf.switch_to_window(wf.window_handles)  # 切回页面操作

    ad = wf.find_element_by_id("loginGrayLayoutImg")  #账号登出
    ActionChains(wf).move_to_element(ad).perform()
    time.sleep(1)
    wf.find_element_by_id("loginGrayOut").click()
    time.sleep(2)


wf=webdriver.Firefox()
qqlo('1061502896','password')
test = wf.current_url
if test == "http://www.qq.com/":
    print("pass")
else:
    print("fail")
time.sleep(2)
qqlout()
time.sleep(1)
wf.quit()
