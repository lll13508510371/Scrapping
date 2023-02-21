from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 浏览器配置选项功能

chrome_options = Options()  # 声明一个谷歌配置对象
chrome_options.add_argument('--headless')  # 添加 无头模式 配置

# 创建浏览器对象的时候添加配置
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.baidu.com')
print(driver.page_source)

input()
driver.quit()

"""
selenium的无头模式一般在项目写完后添加

优点:
    1.运行的速度相对块

缺点:
    某些页面必须的经过浏览器渲染（一些浏览器播放器播放按扭设置了一些前端框架，无头模式播放比了）
"""