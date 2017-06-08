#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
#导入键盘模块
from selenium.webdriver.common.action_chains import ActionChains
#导入鼠标事件模块
wf=webdriver.Firefox()

wf.get("http://www.baidu.com")
time.sleep(2)
ab=wf.find_element_by_link_text("设置")
ActionChains(wf).move_to_element(ab).perform()  #鼠标悬停操作
#wf.find_element_by_link_text("设置").click()
time.sleep(2)
#wf.find_element_by_link_text("关闭预测").click()
yy=wf.find_element_by_link_text("关闭预测")
ActionChains(wf).move_to_element(yy).click().perform()
time.sleep(2)
wf.find_element_by_id("kw").send_keys("hello world")
time.sleep(2)
wf.find_element_by_id("kw").submit()
#wf.find_element_by_id("kw").send_keys(Keys.ENTER)
#use id to find the element we need, type hello world into the search
#time.sleep(2)
#wf.find_element_by_id("su").click()
time.sleep(3)
wf.back()
#wf.find_element_by_partial_link_text("新").click()
#wf.find_element_by_id("su").click()
time.sleep(3)
wf.quit()