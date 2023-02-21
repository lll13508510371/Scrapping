import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能


driver = webdriver.Chrome()

driver.get('https://www.baidu.com/')
time.sleep(3)

driver.get('https://news.baidu.com/')
time.sleep(3)

driver.back()  # 后退到上一级页面
time.sleep(3)

driver.forward()  # 前进到下一级页面
time.sleep(3)


driver.refresh() # 刷新当前页面

input()  # 阻塞程序
driver.quit()

