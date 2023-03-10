"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
"""

tel = '18123115458'

tel_1 = """1812311545811
        118
      """

import re

content = re.findall('^\d{3}(\d*)\d{4}$', tel, re.S)
# content = re.findall('\d{3}(\d*)\d{4}', tel, re.S) #因为是精确匹配，所以这里这样也行，只不过逻辑没那么清晰
''' 
--> .*? 取到空字符串 没太懂 不有约束吗？ 
--> 思考后
    这种情况应该是元字符不是约束字符 
    导致？非贪婪模式零次匹配--> 因为是*，零次匹配也能匹配到空字符串''，所以返回空字符串列表 如果是+直接返回空列表
'''

substitute_content = re.sub(content[0], '****', tel)
# content = re.findall('1.*?1', tel_1, re.S)

# 用除了'.'意外以外的其它元字符，不会将所有的字符都匹配下来，具体情况具体看 （e.g. 如下）
# *允许元字符 一开始就没有匹配到数据（匹配0次），这个时候就返回一个空字符串
# 当元字符匹配完数据，之后没有匹配到数据，就返回这个列表字符串元素
# content = re.findall('11\s+', tel_1, re.S)
# content = re.findall('11\s*', tel_1, re.S)
print(content)
print(substitute_content)
'''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
用+如果没有数据会直接返回空列表
--> e.g.
content = re.findall('\d{3}\s+\d{4}', tel, re.S) --> s+ 被当作None(精确匹配的时候返回的是空列表[])来处理了，所以什么也匹配不到  --> 没有出现过空白，返回空列表
content = re.findall('\d{3}\s*\d{4}', tel, re.S) --> s* 被当作''空字符串（因为在精确匹配的时候返回的是['']）来处理，所以还是能够匹配数据 --> *允许匹配零次，所以会返回一个空字符串
'''