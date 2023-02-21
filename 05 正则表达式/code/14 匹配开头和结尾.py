
import re

email_list = ["xiaoWang@163.com", "xiaoWang@163.comheihei", ".com.xiaowang@qq.com"]

'''
^ $ 限制了开头结尾，如果有其它的数据，那么就会匹配不到数据，得到 None (没有匹配到数据）
'''

for email in email_list:
    result = re.match('^\w*@.+\.com$', email)
    '''
    result = re.match('^\w*@.+.com$', email) 这样写也行，是特殊字符'.'把邮箱的那个'.'匹配到了
    正确的做法还是应该用'\.'来代表那个邮箱的'.'
    '''
    # print(result.group())
    if result:
        print(f'{email} 是规范的邮箱地址, 地址是: {result.group()}')

    else:
        print(f'{email} 不是规范的邮箱地址')

''' \w一定要没有字符才能匹配到数据，否则得到的就是空类型类的对象(None） 空类型类的对象(None)没有group() '''
# result = re.match('\w*@.+.com', email_list[2])
# print(result.group())



