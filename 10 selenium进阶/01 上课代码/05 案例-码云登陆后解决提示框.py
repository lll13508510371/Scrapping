import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 导入定位器功能

driver = webdriver.Chrome()
driver.get('https://gitee.com/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR, '.item.git-nav-user__login-item').click()
driver.find_element(By.CSS_SELECTOR, '#git-login #user_login').send_keys('2535513449@qq.com')
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#user_password').send_keys('hjx_3136419')
time.sleep(2)
driver.find_element(By.NAME, 'commit').click()

"""坐标点点击提示框"""

# 坐标点击前需要时间渲染页面
time.sleep(3)
# move_by_offset() 根据坐标点点击
# context_click 右键单击
# click 单击
# ActionChains(driver).move_by_offset(1072, 855).context_click().perform()
ActionChains(driver).move_by_offset(1072, 855).click().perform()


input()  # 阻塞程序
driver.quit()
