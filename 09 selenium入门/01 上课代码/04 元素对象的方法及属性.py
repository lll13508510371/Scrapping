import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能


driver = webdriver.Chrome()

driver.get('https://www.douban.com/')


"""
text    属性, 可以提取标签对象包含的文本内容, 支持链式调用
"""
result8 = driver.find_element(By.CSS_SELECTOR, '.lnk-app')
contend = result8.text
print(contend)

"""
get_attribute(属性名)
    方法, 可以根据属性名提取该标签属性对应的值, 支持链式调用
    
"""
result9 = driver.find_element(By.CSS_SELECTOR, '.lnk-app').get_attribute('href')
print(result9)

"""处理输入框数据输入"""
# 1.找到输入框对应的标签对象
# 2.调用 send_keys('输入的字符串') 网输入框中输入字符串数据, 支持链式调用
driver.find_element(By.CSS_SELECTOR, '.anony-srh .inp>input').send_keys('流浪地球2')


"""标签的点击操作"""
"""
click() 执行标签的点击事件操作, 需要该标签具有点击事件
"""
driver.find_element(By.CSS_SELECTOR, '.bn>input').click()

input()  # 阻塞程序
driver.quit()

