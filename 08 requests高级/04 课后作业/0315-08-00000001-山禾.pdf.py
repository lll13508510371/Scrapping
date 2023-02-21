import csv
import time

import requests


def get_time():
    current_time = str(int(time.time() * 1000))

    return current_time


url = 'https://index.mysteel.com/api/pricetrend/getChartMultiCity.htm?'

'''
！！！
params 当中的数据是url编码数据，在网页当中看解码之后的内容还是没有显示出中文（因为我们看到和选择的内容是中文的，正常情况下看解密url的数据应该是中文）
，应该是加密了，这里没有问题，就算是加密了，但我们传的是url编码的数据，计算器是能够识别的，所以这里加不加密都没问题
'''
params = {
    'catalog': '%E8%A7%92%E9%92%A2_:_%E8%A7%92%E9%92%A2',
    'city': '%E9%95%BF%E6%B2%99',
    'spec': 'Q235B%2050*50*5_:_Q235B_50*50*5',
    'startTime': '2023-01-01',
    'endTime': '2023-02-01',
    'callback': 'json',
    'v': get_time()
}

response = requests.get(url=url, params=params)

data = response.json()

data_2 = data['data'][0]['dateValueMap']
# print(data_2)
Cityname = data['data'][0]['lineName']
# print(Cityname)

data_3 = [{'Cityname': Cityname, 'Data': i['date'], 'Value': i['value']} for i in data_2]
# print(data_3)

with open('data.csv', mode='w', encoding='utf-8') as f:
    csv_dicwriter = csv.DictWriter(f, fieldnames=['Cityname', 'Data', 'Value'])
    csv_dicwriter.writeheader()

    for data_4 in data_3:
        csv_dicwriter.writerow(data_4)
