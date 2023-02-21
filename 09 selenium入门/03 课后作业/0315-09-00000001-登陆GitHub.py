"""
目标网址: https://github.com/login 模拟登录
(https://github.com 我爬这个）

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

driver.get('https://github.com')

driver.implicitly_wait(10)

driver.find_element(By.LINK_TEXT, 'Sign up').click()
time.sleep(3)

driver.find_element(By.LINK_TEXT, 'Sign in →').click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '#login_field').send_keys('p1908189@gmail.com')
time.sleep(2)

'''
真的是要注意隐私，交作业突然就想起密码别跟着提交了，很多时候想着对方应该是值得信任的，一些重要的东西就是这么无意识下就泄露出去了
（虽然山禾应该是不会看的，只是作业而已，但很多时候就是这么想，可能你觉得值得信任的人他就是会这么做）
'''
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('lll13765959090')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-block.js-sign-in-button').click()

'''
input阻塞程序，像这样的模拟登陆，最后登陆点击就会关闭浏览器就很怪，要么设置等待时间，登陆进去之后等待一段时间再关闭
'''
input()

driver.quit()
