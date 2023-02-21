"""
目标网址: https://www.ku6.com/detail/71

作业要求:
    1.用 selenium 采集所需要的数据
    2.需要数据如下所示
        title 视频的标题
        img_url 视频图片对应的url地址
        detail_url 视频详情页url地址
    3.保存为csv数据
请在下方编写代码
"""
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.ku6.com/detail/71')

driver.implicitly_wait(10)

title_list = driver.find_elements(By.XPATH, '//div[@class="video-item"]/div[2]//a')
# print(title_list)

detail_url_list = driver.find_elements(By.CSS_SELECTOR, '.video-item h3>a')
# print(detail_url_list)

img_url_list = driver.find_elements(By.XPATH, '//div[@class="video-image-container"]//img')
# print(img_url_list)

with open('酷六.csv', mode='w', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['title', 'detail_url', 'img_url'])
    writer.writeheader()

    '''不能通过这样的方式取值，错误的方式，正确方式（前提是列表长度都相同）是通过1. zip()组包 或者 2. 根据长度(len)从列表当中取值 '''
    # for tit, deti_url, im_url in title_list, detail_url_list, img_url_list:

    for tit, deti_url, im_url in zip(title_list, detail_url_list, img_url_list):
        title = tit.text
        detail_url = deti_url.get_attribute('href')
        img_url = im_url.get_attribute('src')
        data_dic = {
            'title': title,
            'detail_url': detail_url,
            'img_url': img_url
        }
        writer.writerow(data_dic)

# input()

driver.quit()
