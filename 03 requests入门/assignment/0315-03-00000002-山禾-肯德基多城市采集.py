"""
    - 课上肯德基案例, 将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""

import requests

params = {
    'op': 'keyword'
}


def get_data(city, i):
    data = {
        'cname': '',
        'pid': '',
        'keyword': city,
        'pageIndex': i,
        'pageSize': 10,
    }
    return data

'''
'pageIndex': i   i可以传数字也可以传字符串
'''

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

print('------北京门店-------')
for i in range(1, 18):
    response = requests.post(url=url, params=params, data=get_data('北京', i))
    json_data = response.json()
    # print(type(json_data))
    store_data = json_data['Table1']
    for store in store_data:
        print(store['rownum'], store['storeName'], store['addressDetail'], store['pro'], sep=' | ')

print('''-----上海门店-------''')
for i in range(1, 15):
    response = requests.post(url=url, params=params, data=get_data('上海', i))
    json_data = response.json()
    store_data = json_data['Table1']
    for store in store_data:
        print(store['rownum'], store['storeName'], store['addressDetail'], store['pro'], sep=' | ')

print('-----广州门店-------')
for i in range(1, 6):
    response = requests.post(url=url, params=params, data=get_data('广州', i))
    json_data = response.json()
    store_data = json_data['Table1']
    for store in store_data:
        print(store['rownum'], store['storeName'], store['addressDetail'], store['pro'], sep=' | ')
# response = requests.post(url=url, params=params, data=get_data(1))
# # print(response.text)
# json_data = response.json()
# print(json_data)
