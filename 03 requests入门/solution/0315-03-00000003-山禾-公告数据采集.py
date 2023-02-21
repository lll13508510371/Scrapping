"""
    目标网址: http://www.zfcg.sh.gov.cn
    作业要求:
            1. 点击页面导航栏中 "采购公告" 栏目
            2. 采集下面公告信息数据, 需要采集以下数据:
                title  公告标题
                url    公告详情页地址
                districtName 公告区域
            3. 采集完后打印输出即可
请在下方完成代码:
"""
import requests

json_data = {
    "utm": "sites_group_front.2ef5001f.0.0.68c445a091a811ed86153d517295ea20",
    "categoryCode": "ZcyAnnouncement3012",
    "pageSize": 15,
    "pageNo": 1
}
url = 'http://www.zfcg.sh.gov.cn/front/search/category'
response = requests.post(url=url,
                         json=json_data)
json_data = response.json()
print(json_data)

data_list = json_data['hits']['hits']

for data_ in  data_list:
    title = data_['_source']['title']
    url_ = data_['_source']['url']
    districtName = data_['_source']['districtName']
    print(title, url_, districtName, sep=' | ')


