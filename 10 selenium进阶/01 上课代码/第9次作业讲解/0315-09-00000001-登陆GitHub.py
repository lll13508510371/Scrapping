"""
目标网址: https://github.com/login 模拟登录

作业要求:
    1.用 selenium 模拟登录GitHub(首先自己注册一个账号)
温馨提示:
    这个网站加载速度很慢, 最好设置时间长一点的等待
请在下方编写代码
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://github.com/login')
driver.implicitly_wait(10)
driver.maximize_window()

"""模拟登陆"""

# 输入用户名
driver.find_element(By.CSS_SELECTOR, '#login_field').send_keys('hjx-edu')
time.sleep(2)

# 数据密码
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('qingdeng123')

# 点击登陆
driver.find_element(By.CSS_SELECTOR, '#login > div.auth-form-body.mt-3 > form > div > input.btn.btn-primary.btn-block.js-sign-in-button').click()




input()
driver.quit()
