"""
    - 课上肯德基案例, 将北京,上海,广州三个城市的门店信息获取下来
	- 获取下来的信息用print函数打印即可
	
请在下方实现代码:
"""
import requests


def get_page(city_name):
    """传入城市名返回城市有多少页"""
    data = {
        'cname': '',
        'pid': '',
        'keyword': city_name,
        'pageIndex': '1',
        'pageSize': '10',
    }
    response = requests.post(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                  data=data)
    json_data = response.json()
    count = json_data['Table'][0]['rowcount']
    # print(count)
    # print(type(count))

    if count % 10 > 0:
        page_num = count // 10 + 1
    else:
        page_num = count // 10
    return page_num

def get_data(city):
    page_num = get_page(city)

    print(f'============正在获取{city}地区的数据============')
    for page in range(1, page_num + 1):
        data = {
            'cname': '',
            'pid': '',
            'keyword': city,
            'pageIndex': str(page),
            'pageSize': '10',
        }

        response = requests.post(url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword',
                                 data=data)
        json_data = response.json()
        # print(json_data)

        # 解析数据
        data_list = json_data['Table1']
        # print(len(data_list))
        for dat in data_list:
            storeName = dat['storeName']
            provinceName = dat['provinceName']
            addressDetail = dat['addressDetail']
            pro = dat['pro']
            print(storeName, provinceName, addressDetail, pro, sep=' | ')


if __name__ == '__main__':
    all_city = ['北京','上海','广州']
    # print(get_page('上海'))
    for city in all_city:
        get_data(city)






