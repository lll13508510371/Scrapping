import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能

driver = webdriver.Chrome()

driver.get('https://www.douban.com/')

# 点击 "读书分类"
driver.find_element(By.CSS_SELECTOR, '.lnk-book').click()

windows = driver.window_handles
print(windows)

time.sleep(3)

"""切换到其他窗口"""
# switch_to.window 指定窗口对象列表的索引切换窗口
driver.switch_to.window(windows[0])  # 切换到第一个窗口

time.sleep(3)
driver.switch_to.window(windows[1])

input()  # 阻塞程序
driver.quit()
