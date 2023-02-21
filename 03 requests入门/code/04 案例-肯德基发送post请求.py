import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

params = {'op': 'keyword'}

# 构建请求参数字典
data = {
    'cname': '',
    'pid': '',
    'keyword': '北京',
    'pageIndex': '1',
    'pageSize': '10',
}
# data 关键字是构建post请求的查询参数关键字
response = requests.post(url=url, params=params, data=data)
json_data = response.json()
print(json_data)

# 解析数据
data_list = json_data['Table1']
print(len(data_list))
for dat in data_list:
    storeName = dat['storeName']
    provinceName = dat['provinceName']
    addressDetail = dat['addressDetail']
    pro = dat['pro']
    print(storeName, provinceName, addressDetail, pro, sep=' | ')
