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

url = 'http://www.zfcg.sh.gov.cn/front/search/category'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN, zh;q = 0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '135',
    'Content-Type': 'application/json',
    'Cookie': '_zcy_log_client_uuid = 5f82a930-90f1-11ed-9b6e-bb85f5f0e66d',
    'Host': 'www.zfcg.sh.gov.cn',
    'Origin': 'http://www.zfcg.sh.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://www.zfcg.sh.gov.cn/ZcyAnnouncement/index.html?utm = sites_group_front.2ef5001f.0.0.5f842fd090f111ed9b6ebb85f5f0e66d',
    'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_15_7) AppleWebKit/537.36(KHTML, likeGecko) Chrome/108.0.0.0Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_json_pamarm(i):
    json_pamarm = {
        'categoryCode': ''"ZcyAnnouncement3012"'',
        'pageNo': 1,
        'pageSize': 15,
        'utm': '"sites_group_front.2ef5001f.0.0.5f842fd090f111ed9b6ebb85f5f0e66d"'
    }

    return json_pamarm


'''
老是忘记返回值
'''

for i in range(1, 99):
    response = requests.post(url=url, json=get_json_pamarm(i))
    json_data = response.json()
    list_data = json_data['hits']['hits']
    print(list_data)
    for j in list_data:
        url_data = j['_source']['url']
        title = j['_source']['title']
        districtName = j['_source']['districtName']
        print(url_data, title, districtName, sep=' | ')
