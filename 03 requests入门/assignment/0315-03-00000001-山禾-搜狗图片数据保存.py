"""
	- 课上的搜狗图片案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存到文件夹里面
	有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		
请在下方编写代码
"""
import os
import time
import requests

url = 'https://pic.sogou.com/napi/pc/searchList'

headers = {
    'Cookie': 'IPLOC=CN; SUID=3061DA088330A40A0000000063BCCF4C; SUV=1673318221158855; SNUID=4414AE7D757085AAB72F62F575BF5DDA; wuid=1673318224839; FUV=7d1b2f19a01a18355461ba69d3e4dc64; search_tip=1673318236704; ABTEST=0|1673319313|v1',
    'Host': 'pic.sogou.com'

}


def get_param(i):
    params = {
        'mood': '7',
        'dm': '0',
        'mode': '1',
        'start': i * 48,
        'xml_len': '48',
        'query': '风景'
    }
    return params


''' Python 是强类型语言，底层字符串和数字能相互转化，例如上面i * 48
    就是数字转化成字符串
    --> 不对不对，字典值本来就可以取数字
'''

path = '/Users/lujinghan/PycharmProjects/scrapping/03 requests入门/assignment/img'
if not os.path.exists(path):
    os.mkdir(path)

for i in range(3):
    print(f'------------正在下载第{i + 1}页数据------------')
    response = requests.get(url=url, params=get_param(i), verify=False)
    json_data = response.json()
    img_list = json_data['data']['items']
    # print(img_list)
    for j in img_list:
        img_url = j['locImageLink']
        print(img_url)
        file_name = img_url.split('/')[-1]
        try:
            time.sleep(0.1)
            img_content = requests.get(img_url).content
            # with open(os.path.join(path, file_name), mode='wb') as f:
            # 有些大图片content好像有问题，有些保存不下来，就用try except跳过
            # 小图片保存没问题，都能保存下来
            with open(path + '/' + file_name + '.png', mode='wb') as f:
                f.write(img_content)
                print('图片保存完成')
        except Exception as e:
            pass
