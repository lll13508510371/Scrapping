import base64
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from constants import FENG_PASSWORD, FENG_USERNAME

driver = webdriver.Chrome()
driver.get('https://www.ifeng.com/')
driver.implicitly_wait(10)
driver.maximize_window()

"""页面右上角点击登陆"""
driver.find_element(By.CSS_SELECTOR, '.login_in_2x-3NxtSKIw').click()
time.sleep(2)

"""点击账号登陆, 需要切换到嵌套网页"""
iframe_obj = driver.find_element(By.CSS_SELECTOR, '.box-1pZSPyeN>div>iframe')
driver.switch_to.frame(iframe_obj)
# 点击登陆
driver.find_element(By.CSS_SELECTOR, '.tab-2sXGklBv>span:nth-child(1)').click()
time.sleep(1)

"""输入用户信息"""
driver.find_element(By.CSS_SELECTOR, '.loginById-3HzkdnTl>div>div>input').send_keys(FENG_USERNAME)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '.input-2gdDY-Gz>div>input').send_keys(FENG_PASSWORD)
time.sleep(1)

# 处理验证码
img_src = driver.find_element(By.CSS_SELECTOR, '.codeImg-2pONyHUT>img').get_attribute('src')
print('img标签的src属性值:', img_src)

img_str = img_src.split(',')[-1]
print('base64字符串形式的图片: ', img_str)
bytes_img = base64.b64decode(img_str)
with open('yzm.png', mode='wb') as f:
    f.write(bytes_img)
    print('验证码保存完毕!!!')

"""调用打码平台识别验证码"""
from img_api import base64_api

result = base64_api('yzm.png', typeid=7)
print('验证码识别结果:', result)

# 输入验证码
driver.find_element(By.CSS_SELECTOR, '.input-2N0ut5SW>div>input').send_keys(result)
time.sleep(2)

# 点击登陆
driver.find_element(By.CSS_SELECTOR, '.submmitBtn-2AmMFR0C').click()

input()
driver.quit()