"""
按照以下网址爬取小说。爬取《剑来》前面五章的小说数据,分别保存在不同的txt文件下

	-- 网址： https://www.bige7.com/book/1031/

请下下方开始编写代码
"""
# 爬取小说-->爬取的一章小说数据
import os
import requests
import re


def get_one_zhangjie(url, times=3):  # times 控制异常重试的次数, 超过了异常重试指定的次数, 代码仍然会报错
    """保存一章小说的逻辑"""
    try:
        response_2 = requests.get(url)
        html_data_2 = response_2.text
        result_2 = re.findall('<div id="chaptercontent" class=".*?">(.*?)<p class="readinline">.*?</p></div>',
                              html_data_2,
                              re.S)

        contend = result_2[0].replace('<br /><br />', '\n\n').replace('\u3000\u3000', '')

        # 解析章节名:用于保存文件, 作为文件名
        file_name = re.findall('<h1 class="wap_none">(.*?)</h1>', html_data_2, re.S)[0]

        with open('剑来\\' + file_name + '.txt', mode='w', encoding='utf-8') as f:
            f.write(contend)
            print('保存完成:', file_name)

    except Exception as e:
        print(e)
        if times >= 1:
            '''
            这里print也会有三个，因为get_one_zhangjie(url, times=times - 1)递归运行三次，所以放到最后才print出来
            '''
            get_one_zhangjie(url, times=times - 1)  # 利用函数递归的特性, 进行异常重试
            print('**********************************************')


if __name__ == '__main__':

    if not os.path.exists('剑来'):
        os.mkdir('剑来')

    url = 'https://www.bqg70.com/book/1031/'
    response = requests.get(url)
    html_data = response.text
    # print(html_data)

    result = re.findall('<dd><a href ="(.*?)">.*?</a></dd>', html_data, re.S)

    for res in result[:5]:
        # 拼接完整地址
        all_url = 'https://www.bqg70.com' + res
        get_one_zhangjie(all_url)
