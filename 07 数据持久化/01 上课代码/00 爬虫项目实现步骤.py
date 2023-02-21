"""
爬虫项目实现的步骤:

1. 找数据对应的地址(文本 图片 视频 音频), 网页性质的分析 <静态网页/动态网页>
2. 请求地址, 获取地址对相应的数据<js css 图片 视频数据  html  音频数据>
3. 数据筛选, 数据解析, 提取需要的数据, 剔除不要的数据
4. 保存数据(本地, 数据库)  有专门的模块会提供方法保存特定的文件
    txt
    excel -->   openpyxl jwt
    word
    pdf
    png, jpg, ....

    mysql  关系型数据库<高级开发>
    MongoDB  非关系型数据库<爬虫专题>
    redis   缓存性型数据库<爬虫专题>

    数据持久化
"""

