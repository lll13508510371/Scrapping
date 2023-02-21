"""
爬虫项目实现的步骤:

1. 找数据对应的地址(文本 图片 视频 音频), 网页性质的分析 <静态网页/动态网页>
2. 请求地址, 获取地址对相应的数据<js css 图片 视频数据  html  音频数据>
3. 数据筛选, 数据解析, 提取需要的数据, 剔除不要的数据
    css选择器: 专门用来提取html标签中的数据
    正则表达式: 在爬虫中主要针对在小范围的字符串中提取数据
    xpath节点提取: 专门用来提取html标签中的数据

4. 保存数据(本地, 数据库)
"""

# beautifulSoup4  --> bs4  用的Python模块不一样 <beautifulSoup4>
# 数据解析主要的是在结构化数据(表单数据）和半结构化数据（e.g. json)中提取数据内容

