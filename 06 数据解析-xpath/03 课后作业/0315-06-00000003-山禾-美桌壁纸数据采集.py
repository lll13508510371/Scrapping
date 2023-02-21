"""
    目标网址: http://www.win4000.com/zt/dongman.html
    
    需求:
        "动漫桌面壁纸" 文字下面有很多动漫图集
        1、用xpath采集数据
        2、采集以下信息
            采集动漫图集的标题
            采集动漫图集中图片对应的url地址
            
        解析到数据用print()函数打印即可
请在下方编写代码：
"""

import os
import time

import parsel
import requests

'''这网站要cookie，cookie一段时间之后会过期，然后会有新的cookie，这个时候需要换一下'''
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Referer': 'http://www.win4000.com/zt/dongman.html',
    'host':'www.win4000.com',
    'Cookie': 't=4e4256b831ff30cc0f7af448674fc656; r=5927; t=d764b1db09b47d1b3a6f54bff3edb023; r=256'
}

response = requests.get('http://www.win4000.com/zt/dongman.html', headers=headers)

response.encoding = response.apparent_encoding

html_data = response.text
# print(html_data)

selector = parsel.Selector(html_data)

lis = selector.xpath('//div[@class="w1180 clearfix"]//ul[@class="clearfix"]/li')
# print(lis)

for li in lis:
    title = li.xpath('./a/p/text()').get()

    '''
    如果没有img_2,要先创建了img_2路径才能进行img_2/{title}这样的操作，不能通过img_2/{title}这样的方式直接创建出两个目录，会报错
    '''
    if not os.path.exists(f'/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img_2'):
        os.mkdir(f'/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img_2')
    if not os.path.exists(f'/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img_2/{title}'):
        os.mkdir(f'/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img_2/{title}')

    pic_set_url = li.xpath('./a/@href').get()  # get()得到的是str
    # print(pic_sets)
    pic_html_data = requests.get(url=pic_set_url, headers=headers).text

    pic_selector = parsel.Selector(pic_html_data)

    pics_url_list = pic_selector.xpath('//div[@class="scroll-img-cont "]//li//img/@data-src').getall()

    # print(title, pics_url_list)

    for pic_url in pics_url_list:
        print(pic_url)
        pic_name = pic_url.split('/')[-1]
        # print(pic_name)

        pic_content = requests.get(pic_url).content
        # print(pic_content)

        with open(f'/Users/lujinghan/PycharmProjects/scrapping/06 数据解析-xpath/03 课后作业/img_2/{title}/{pic_name}',
                  mode='wb') as f:
            print(f'正在保存{pic_name}...')
            f.write(pic_content)
            print('保存完成')

'''图片url找img标签'''
'''
这里三个url的请求头是可以共用的，里面只要不添加host就行，因为第三个图片url的host和前两个的不一样，添加会导致请求不到图片数据
但三个图片url如果不加headers应该是有反爬措施的，得到的图片二进制数据全是一样的，而且图片打不开
'''