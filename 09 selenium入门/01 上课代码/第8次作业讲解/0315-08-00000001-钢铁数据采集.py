import csv

import requests

url = 'https://index.mysteel.com/api/pricetrend/getChartMultiCity.htm'
params = {
    'catalog': '%E8%A7%92%E9%92%A2_:_%E8%A7%92%E9%92%A2',
    'city': '%E9%95%BF%E6%B2%99',
    'spec': 'Q235B%2050*50*5_:_Q235B_50*50*5',
    'startTime': '2023-01-01',
    'endTime': '2023-02-01',
    'callback': 'json',
    'v': '1675683738571',
}

response = requests.get(url=url, params=params)
json_data = response.json()
print(json_data)

city_name = json_data['data'][0]['lineName']
print(city_name)

list_data = json_data['data'][0]['dateValueMap']

with open('data.csv', mode='a', encoding='utf-8', newline='') as f:
    csv_write = csv.DictWriter(f, fieldnames=['city_name', 'date', 'value'])
    csv_write.writeheader()  # 表头只需要写入一次

    for data_ in list_data:
        data_['city_name'] = city_name
        print(data_)

        csv_write.writerow(data_)
