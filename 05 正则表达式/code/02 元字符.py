text = """
回复_(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com


2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
397872410@qq.com，谢谢楼主
"""
import re

"""
书写的正则表达式规则, 会把所有的约束字符和规则匹配到的数据一并返回

.  在默认情况下, 匹配除了换行符以外的任意字符串
re.S  模式匹配, 能够让 . 匹配到换行符
"""

result = re.findall('Super劫Zed: .................', text, re.S)
print(result)
print('=' * 50)

"""
\d  匹配一个数字字符
\D  匹配一个非数字字符
"""
result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d\d', text, re.S)
print(result)

result = re.findall('Super劫Zed: \d\d\d\d\d\d\d\d\d\D', text, re.S)
print(result)
print('=' * 50)

"""
\s  匹配一个空白字符(换行  制表符   空格  )
\S  匹配一个非空白字符
"""
result = re.findall('\s', text, re.S)
print(result)

result = re.findall('\S', text, re.S)
print(result)
print('=' * 50)

"""
\w  匹配一个单词字符 a-z A-Z _  也包含了各个国家地区文字--> 因为互联网的原因
\W  匹配一个非单词字符     空白字符和符号
"""
result = re.findall('\w', text, re.S)
print(result)

result = re.findall('\W', text, re.S)
print(result)

print('=' * 50)

"""
+   匹配前一个字符一次或者多次(前一个字符最少要出现一次才能匹配到)
*   匹配前一个字符零次或者多次(前一个字符可以没出现)

多次匹配一般是搭配元字符使用

.*  匹配任意字符零次或者多次
.+  匹配任意字符一次或者多次
"""
result = re.findall('Super劫Zed: \d*', text, re.S)
print(result)
result = re.findall('Super劫Zed: \d+', text, re.S)
print(result)

print('---------')
result = re.findall('Super劫Zed: \s+', text, re.S)
print(result)
result = re.findall('Super劫Zed:\s+', text, re.S)
print(result)
print('---------')

result = re.findall('Super劫Zed: \s*', text, re.S)
print(result)

print('=' * 50)
