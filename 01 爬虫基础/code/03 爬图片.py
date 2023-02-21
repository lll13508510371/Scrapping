import requests
import re  # 内置模块, 正则表达式解析模块

response = requests.get('https://www.hexuexiao.cn/a/124525.html')
html_data = response.text
# print(html_data)


# 解析提取数据
# re.findall(解析规则, 解析数据, 解析模式)
"""
<a class="btn btn-default btn-xs" href="https://i.hexuexiao.cn/up/da/75/47/f59543039ce27d69ef5d25b5a04775da.jpg.source.jpg" role="button" target="_blank">
<a class="btn btn-default btn-xs" href="(.*?)" role.*?
"""
result = re.findall('<a class="btn btn-default btn-xs" href="(.*?)" role.*?',
                    html_data,
                    re.S)

print(result)

# 根据解析到的图片地址请求图片数据
img_response = requests.get(result[0])
# 图片, 视频, 音频 都属于二进制数据
img_data = img_response.content  # content 从响应体对象中提取二进制数据
# print(img_data)

file_name = result[0].split('/')
print(file_name)

with open(file_name, mode='wb') as f:
    f.write(img_data)
