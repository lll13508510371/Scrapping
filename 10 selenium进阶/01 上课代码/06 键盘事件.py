# 在百度搜索框输入  python ，全选,复制,剪切,粘贴 跳转到搜狗输入框进行搜索

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 导入定位器功能
from selenium.webdriver.common.keys import Keys  # 导入键盘事件

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('python')
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'a')  # 全选
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'c')  # 复制
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'x')  # 剪切
time.sleep(3)

driver.get('https://www.sogou.com/index.php')

driver.find_element(By.CSS_SELECTOR, '#query').send_keys(Keys.CONTROL, 'v')  # 粘贴
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#query').send_keys(Keys.ENTER)
# driver.find_element(By.CSS_SELECTOR, '#stb').send_keys(Keys.ENTER)
'''
driver.find_element(By.CSS_SELECTOR, '#stb') 找到的是点击按钮，正常情况是输入框输入内容后
然后在输入框当中按回车，但这里找到输入框键盘回车也能跳转到新的页面
例如goole搜索页面就没有点击按钮，就是输入框进行回车跳转页面
'''

input()  # 阻塞程序
driver.quit()
