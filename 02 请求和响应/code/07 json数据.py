
"""json数据"""

# 作用: json数据是目前主流的数据交换格式(结构清晰, 方便取值)

# 形式: 外层 --> {} 或 []   内层可以嵌套数据
# {字段1: 值1, 字段2: [{嵌套字段1: 嵌套字段值1}, {}, {}, {}......]}
# json数据是具有特殊形式的字符串
# 字段和值都是用双引号包裹, 如果是单引号, 那不是规范的json数据

"""
在json数据中, 值必须是以下数据类型

字符串
数字
对象(json对象)<嵌套形式>
数组
布尔值
null
"""

import requests

response = requests.get('https://news.163.com/special/yaowen_channel_api/?callback=channel_callback&date=0120')

print(response.text)

# 通过 json() 提取json数据之后, 会在底层经过数据转换, 转换成一个对象, 具体类型根据最外层字符串符号确定
# 获取响应体的json数据, 如果数据不是json数据, 使用json()方法提取会报错
print(type(response.json()))



