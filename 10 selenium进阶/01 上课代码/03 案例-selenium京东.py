import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def search_product(key):
    """指定关键字搜索商品数据"""
    # 定位搜索框输入搜索的关键字
    # clear() 清空输入框数据
    input_label = driver.find_element(By.CSS_SELECTOR, '#key')
    # input_label.send_keys('哈哈')
    input_label.send_keys(key)

    time.sleep(1)
    # 点击搜索按钮
    driver.find_element(By.CSS_SELECTOR, '.button').click()


def drop_down():
    """模拟用户进行页面滚动操作"""
    for h in range(1, 11, 2):  # h --> 13579
        time.sleep(0.5)  # 加强制等待, 等待数据渲染
        j = h / 9  # 1/9   3/9  5/9  7/9  9/9
        js_all = f'document.documentElement.scrollTop = document.documentElement.scrollHeight*{j}'
        driver.execute_script(js_all)


def parse_data():
    """解析数据函数"""
    lis = driver.find_elements(By.CSS_SELECTOR, '.gl-item')

    for li in lis:
        title = li.find_element(By.CSS_SELECTOR, 'div.p-name a em').text  # 商品标题
        title = title.replace('京品电脑', '').replace('爱心东东', '').replace('\n', '')

        price = li.find_element(By.CSS_SELECTOR, 'div.p-price strong i').text  # 商品价格
        deal = li.find_element(By.CSS_SELECTOR, 'div.p-commit strong a').text  # 评价数据量
        name = li.find_element(By.CSS_SELECTOR, 'span.J_im_icon a').get_attribute('title')  # 店铺名称
        print(title, price, deal, name, sep=' | ')

        with open('某东.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([title, price, deal, name])


def get_next():
    """点击下一页按钮"""
    driver.find_element(By.CSS_SELECTOR, '.pn-next>em').click()


if __name__ == '__main__':

    keyword = input('请输入您要查找商品的关键字:')

    driver = webdriver.Chrome()
    driver.get('https://www.jd.com/')
    driver.implicitly_wait(10)
    driver.maximize_window()

    # 调用商品搜索的功能函数
    search_product(keyword)

    for i in range(100):
        # 调用滚动页面的函数
        drop_down()

        # 调用解析数据的函数
        parse_data()

        # 调用下一页函数
        get_next()

    input()
    driver.quit()

'''

JD 那里面的页面有异步加载的动态数据，所以需要滚动到最下面加载出来这些数据再拿数据
（但应该不是ajax异步加载动态数据，ajax技术的使用场景是在一个页面当中能够不刷新页面加载出所有数据，但jd这个是有很多页面，每一页有一些异步加载的动态数据）
'''
