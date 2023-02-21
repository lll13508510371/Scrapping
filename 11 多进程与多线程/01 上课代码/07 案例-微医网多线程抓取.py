import csv
import threading

import parsel
import requests

# # 找地址
# url = 'https://www.guahao.com/expert/61409/%E5%86%85%E7%A7%91'
#
# # 发送请求
# response = requests.get(url=url)
# html_data = response.text
# # print(html_data)  # 要确认数据是请求到了
#
# # 解析数据
# selector = parsel.Selector(html_data)
# lis = selector.css('.g-doctor-item')  # 提取所有li标签
# # print(lis)
#
# for li in lis:
#     doctor_name = li.css('div>a>img::attr(title)').get()  # 姓名
#     doctor_level = li.css('dl dt::text').getall()[1].strip()  # 级别
#     doctor_kind = li.css('dd p:nth-child(1)::text').get()  # 科室
#     doctor_Belonging = li.css('dd p:nth-child(2)>span:nth-child(1)::text').get()  # 所属医院
#     doctor_score = li.css('dd p:nth-child(3)>span em::text').get()  # 评分
#     doctor_inquiry = li.css('dd p:nth-child(3)>span i::text').get()  # 问诊量
#     doctor_goodFor = li.css('.skill>p::text').get()  # 擅长
#     doctor_goodFor = doctor_goodFor.replace('\n', '').replace(' ', '')  # 规整数据
#
#     pic_see_price = li.css('.infos.image span em:nth-child(2)::text').get()  # 图文问诊价格
#     if pic_see_price:
#         pic_see_price = pic_see_price.strip()
#
#     print(pic_see_price)


lock = threading.Lock()


def send_request(url):
    response = requests.get(url=url)
    return response.text


def parse_data(data):
    selector = parsel.Selector(data)
    lis = selector.css('.g-doctor-item')  # 提取所有li标签
    # print(lis)

    data_list = []  # 定义一个空列表用于收集每一页数据
    for li in lis:
        doctor_name = li.css('div>a>img::attr(title)').get()  # 姓名
        doctor_level = li.css('dl dt::text').getall()[1].strip()  # 级别
        doctor_kind = li.css('dd p:nth-child(1)::text').get()  # 科室
        doctor_Belonging = li.css('dd p:nth-child(2)>span:nth-child(1)::text').get()  # 所属医院
        doctor_score = li.css('dd p:nth-child(3)>span em::text').get()  # 评分
        doctor_inquiry = li.css('dd p:nth-child(3)>span i::text').get()  # 问诊量
        doctor_goodFor = li.css('.skill>p::text').get()  # 擅长
        doctor_goodFor = doctor_goodFor.replace('\n', '').replace(' ', '')  # 规整数据

        pic_see_price = li.css('.infos.image span em:nth-child(2)::text').get()  # 图文问诊价格
        if pic_see_price:
            pic_see_price = pic_see_price.strip()

        print(doctor_name, doctor_level, doctor_kind, doctor_Belonging, doctor_score,
              doctor_inquiry, doctor_goodFor, pic_see_price)

        data_list.append([doctor_name, doctor_level, doctor_kind, doctor_Belonging, doctor_score,
                          doctor_inquiry, doctor_goodFor, pic_see_price])

    return data_list  # -->二维列表


def save_data(data_list):
    for data in data_list:
        lock.acquire()
        with open('微医网.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow(data)
        lock.release()


def main(url):
    html_data = send_request(url)
    data_list = parse_data(html_data)
    save_data(data_list)


# main('https://www.guahao.com/expert/61409/%E5%86%85%E7%A7%91/p2')

for page in range(1, 39):
    url = f'https://www.guahao.com/expert/61409/%E5%86%85%E7%A7%91/p{page}'

    threading.Thread(target=main, args=(url,)).start()
