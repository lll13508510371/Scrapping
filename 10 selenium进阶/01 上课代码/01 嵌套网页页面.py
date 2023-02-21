from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://music.163.com/#/song?id=1450083773')

"""通过代码切换进入到嵌套网页"""
# 方式1: 根据索引进入到嵌套网页, 索引从 0 开始; 索引值如果超出了目前已有的嵌套网页, 那么程序报错
# driver.switch_to.frame(5)  # frame(5) 切换进入到第一个嵌套网页对应的iframe标签


# 方式2: 根据嵌套网页的 <iframe> 标签对象进入到嵌套网页
iframe = driver.find_element(By.CSS_SELECTOR, '#g_iframe')
driver.switch_to.frame(iframe)

# parent_frame 从子iframe切换到父iframe
driver.switch_to.parent_frame()

print(driver.page_source)  # 打印的就是嵌套网页


input()
driver.quit()


"""
这个数据是不是在嵌套网页?
    1. selenium默认不会回去嵌套网页数据
    2. iframe是嵌套网页对应的标签名字
    3. 如果使用selenium采集数据, 一般第一步是确认有没有嵌套网页, 数据有没有在嵌套网页里面
    4. 常见的在登陆注册页面中经常会使用嵌套网页技术
"""