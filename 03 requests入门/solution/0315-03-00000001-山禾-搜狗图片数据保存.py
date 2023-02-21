"""
	- 课上的搜狗图片案例，先自己实现一遍, 构建查询参数请求数据
	- 将前三页的图片数据保存到文件夹里面
	    有错误需要解决报错<可以根据情况使用（异常捕获 + 请求参数）>
		
请在下方编写代码
"""
import requests
requests.packages.urllib3.disable_warnings()

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

count = 1  # 定义全局变量, 用于命名文件名字
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
        img_url = data['picUrl']
        # print(img_url)

        """保存图片"""
        try:
            img_data = requests.get(url=img_url, verify=False, timeout=3).content  # 请求图片数据
            # file_name = img_url.split('/')[-1]
            # print('file_name', file_name)
            # print('pic\\' + file_name)


            with open('pic\\' + str(count) + '.jpg', mode='wb') as f:
                f.write(img_data)
                print('保存完成:', str(count) + '.jpg')

            count += 1

        except Exception as e:
            print(e)
