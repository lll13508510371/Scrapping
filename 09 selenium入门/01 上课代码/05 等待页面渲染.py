import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能


driver = webdriver.Chrome()

driver.get('https://www.taobao.com/')

# 隐式等待, 括号内部设置等待时间, 单位秒
# 智能化等待, 一旦页面过早的完成了渲染, 那么不会死等下去
driver.implicitly_wait(10)

# 强制等待, 死等
time.sleep(10)

input()  # 阻塞程序
driver.quit()

