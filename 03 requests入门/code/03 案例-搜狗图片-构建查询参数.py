import requests

'''
Ajax 异步请求动态数据 --> 例如网页往下滑加载动态数据，可能第一次加载出来的数据是静态数据
                        要具体看网页源代码   
                        ！！！！都是传参数，因为网站的url没有改变
'''
def get_params(page):
    params = {
        'mode': '1',
        'mood': '7',
        'dm': '0',
        'start': page * 48,
        'xml_len': '48',
        'query': '风景',
    }
    return params


for page in range(3):
    print(f'------------------------正在抓取第{page + 1}页数据----------------------------')
    url = 'https://pic.sogou.com/napi/pc/searchList'
    params = get_params(page)
    response = requests.get(url=url, params=params)
    json_data = response.json()
    # print(json_data)

    # 解析数据
    data_list = json_data['data']['items']
    for data in data_list:
        img_url = data['locImageLink']
        print(img_url)
