import time

from selenium import webdriver  # 导入功能  # pip install selenium


driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

# save_screenshot  截取当前页面图片, 括号内部指定图片的保存路径
# driver.save_screenshot('baidu.png')

# page_source 查看当前页面渲染以后的数据, 极少数情况下会有一个问题
# 问题: 浏览器elements中看到的数据和 selenium 得到的数据有出入
print(driver.page_source)

# with open('a.html', mode='w', encoding='utf-8') as f:
#     f.write(driver.page_source)

# get_cookies  查看页面请求以后的cookies值内容
print(driver.get_cookies())

# 查看当前页面的地址
print(driver.current_url)

# 最大化浏览器
driver.maximize_window()

time.sleep(3)

# 最小化浏览器
driver.minimize_window()

input()  # 阻塞程序
driver.quit()


"""
parsel  
"""