"""
表情包爬取
将此页面下的前五页图片全部获取下来：https://www.biaoqingbao.net/gaoxiao/
"""
import re

"""请下下方开始编写代码"""
import requests

for page in range(1, 6):
    print(f'====================正在抓取第{page}页数据================')
    response = requests.get(f'https://www.biaoqingbao.net/gaoxiao/page_{page}.html')
    html_data = response.text
    print(html_data)

    # 解析数据
    """
    <img class="waitpic" src="https://www.biaoqingbao.net/wp-content/uploads/2020/07/thumb.png" data-original="https://www.biaoqingbao.net/wp-content/uploads/2022/07/006BkP2Hly1h4fpmyuo9yg30500507wh-150x150.gif" alt="二次元跳舞表情包" >
    <img class="waitpic" src="https://www.biaoqingbao.net/wp-content/uploads/2020/07/thumb.png" data-original="(.*?)" alt=".*?" >
    """
    result = re.findall(
        '<img class="waitpic" src="https://www.biaoqingbao.net/wp-content/uploads/2020/07/thumb.png" data-original="(.*?)" alt=".*?" >',
        html_data,
        re.S)

    print(result)
    print(len(result))

    for img_url in result:
        '''肯定是请求数据的时候报错，然后加try except捕捉错误 --> 遇到问题再debug而不是刚开始就想好try，都是慢慢积累的'''
        try:
            # 请求图片数据
            img_data = requests.get(img_url).content

            # 准备一个文件名
            file_name = img_url.split('/')[-1]

            with open('img\\' + file_name, mode='wb') as f:
                f.write(img_data)
                print('保存完成:', file_name)
        except Exception as e:
            pass
'''
下载图片，肯定就不需要查看e的具体异常是什么了（print（e））, 所以直接使用pass
'''