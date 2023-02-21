import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能

driver = webdriver.Chrome()

driver.get('https://gitee.com/')
driver.maximize_window()
driver.minimize_window()
driver.implicitly_wait(10)

# selenium页面的操作, 一定要看的到页面元素
# 点击页面登陆按钮, 进入登陆页面
driver.find_element(By.CSS_SELECTOR, '.item.git-nav-user__login-item').click()

"""输入用户信息"""
driver.find_element(By.CSS_SELECTOR, '#git-login #user_login').send_keys('2535513449@qq.com')
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys('hjx_3136419')
time.sleep(2)


"""点击登陆按钮"""
driver.find_element(By.NAME, 'commit').click()

input()  # 阻塞程序
driver.quit()
