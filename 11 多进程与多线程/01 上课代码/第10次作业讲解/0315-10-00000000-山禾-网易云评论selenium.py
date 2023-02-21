"""
目标网址:https://music.163.com/#/playlist?id=924680166

要求:
	1. 使用selenium
	2. 爬取前面5页的评论数据保存为txt文件
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_data():
    """在每一页中解析数据"""
    divs = driver.find_elements(By.CSS_SELECTOR, '.itm')
    for div in divs:
        contend = div.find_element(By.CSS_SELECTOR, '.cnt.f-brk').text
        print(contend)

        with open('contend.txt', mode='a', encoding='utf-8') as f:
            f.write(contend + '\n')



driver = webdriver.Chrome()
driver.get('https://music.163.com/#/playlist?id=924680166')
driver.implicitly_wait(10)

driver.switch_to.frame(0)
print(driver.page_source)

js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
driver.execute_script(js)

for i in range(5):
    # 调用数据解析函数
    parse_data()

    # 点击下一页
    driver.find_element(By.CSS_SELECTOR, '.znxt').click()

    time.sleep(2)


input()
driver.quit()

