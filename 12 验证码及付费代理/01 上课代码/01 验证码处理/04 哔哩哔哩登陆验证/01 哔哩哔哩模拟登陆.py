import base64
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from constants import BILIBILI_USERNAME, BILIBILI_PASSWORD

driver = webdriver.Chrome()
driver.get('https://passport.bilibili.com/login')
driver.implicitly_wait(10)
driver.maximize_window()

"""输入用户名密码"""
driver.find_element(By.CSS_SELECTOR, '#login-username').send_keys(BILIBILI_USERNAME)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, '#login-passwd').send_keys(BILIBILI_PASSWORD)
time.sleep(2)

"""点击登陆按钮"""
driver.find_element(By.CSS_SELECTOR, '.btn.btn-login').click()

"""selenium 可以根据标签对进行截图"""
time.sleep(2)
# 获取验证码对应的标签
img_obj = driver.find_element(By.CSS_SELECTOR, '.geetest_panel_box.geetest_panelshowclick>div:nth-child(6)')
img_obj.screenshot('yzm.png')
print('正在保存验证码...')
time.sleep(2)

"""识别图片验证码"""
from img_api import base64_api

code_result = base64_api('yzm.png', typeid=21)
print('验证码识别结果为:', code_result)

result_list = code_result.split('|')  # ['202,224', '101,181']

for result in result_list:
    x = result.split(',')[0]  # x轴
    y = result.split(',')[1]  # x轴

    # move_to_element_with_offset  移动到指定的对象点击
    ActionChains(driver).move_to_element_with_offset(img_obj, int(x), int(y)).click().perform()
    time.sleep(1)


# 点击确认
driver.find_element(By.CSS_SELECTOR, '.geetest_panel_box.geetest_panelshowclick>div:nth-child(6) .geetest_commit_tip').click()

input()
driver.quit()
'''
selenium-3.141.0 最新版selenium坐标点击有问题，安装这个版本没问题
'''