import os
import re
import requests
import parsel


def change_title(title):
    """替换非法字符的函数"""
    '''re中[]代表匹配[]当中所有的字符'''
    '''需要转成正则对象，这样[]里面出现的字符只要满足一个就能匹配到，不然得满足[]里面所有的字符才能匹配到'''
    '''这里是因为爬取的图片集文件有特殊符号，所以添加这个，不用每一次爬都添加，爬完之后发现有特殊字符不能创建文件时再用，coding是发现问题再编写相应的代码解决，而不是固定思维'''
    pattern = re.compile('[\\\/\:\*\?\"\<\>\|]')
    new_title = re.sub(pattern, '_', title)
    return new_title

# 1. 找数据地址
url = 'https://www.jdlingyu.com/dm/zb'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# 2.发送请求
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)  # 打印查找数据是否请求到

# 3. 解析数据
# 3.1 解析每一个相册详情页地址
selector = parsel.Selector(html_data)
lis = selector.xpath('//div[@id="post-list"]/ul/li')

for li in lis:
    title = li.xpath('.//h2/a/text()').get()
    href = li.xpath('.//h2/a/@href').get()
    print(title, href)

    # 替换文件夹的非法字符
    new_title = change_title(title)

    if not os.path.exists('img\\' + new_title):
        os.mkdir('img\\' + new_title)

    # 发送详情页的请求
    response_pic = requests.get(url=href, headers=headers).text

    # 解析详情页数据
    selector_pic = parsel.Selector(response_pic)

    # 解析到图片地址列表
    pic_url_list = selector_pic.xpath('//div[@class="entry-content"]/p//img/@src').getall()
    # print(pic_url_list)

    for pic_url in pic_url_list:
        # 根据地址请求图片的二进制数据
        pic_data = requests.get(url=pic_url, headers=headers).content
        # 图片文件名
        pic_name = pic_url.split('/')[-1]

        with open(f'img\\{new_title}\\{pic_name}', mode='wb') as f:
            f.write(pic_data)
            print('保存完成:', pic_name)

'''
需要的数据可能嵌套在一个个页面当中，这个时候就需要嵌套解析数据，这里就进行了两次解析（两个Selector对象）
'''



