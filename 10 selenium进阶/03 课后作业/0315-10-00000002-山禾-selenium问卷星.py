'''
作业要求
1.用selenium自动填写问卷, 自动提交 2.单选题随机选一个选项, 多选题随机选三个选项

目标网址
https://www.wjx.cn/jq/87910206.aspx
'''
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
'''
浏览器检测不单单只是看false，这里这个网页就是false，但最后提交会不成功，这个添加了就成功了
'''
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})

driver.get('https://www.wjx.cn/jq/87910206.aspx')

driver.implicitly_wait(10)
# input()
divs = driver.find_elements(By.CSS_SELECTOR, '.div_question')
# print(len(divs))
# print(divs)

'''
这里不需要设置下滑代码也能下滑点击，应该是定位到了标签，能识别，往下滑动只要能看到相关的内容，就能够进行点击
像之前的码云，虽然定位到了登陆按钮，但看不到，就会报错 --> 元素点击异常   那个情况是窗口没有放大，相应的标签没有在窗口当中
---- >>>>>>>>>>>> 这里还是要下滑，定位到了那个标签之后，只会点击标签当中能看到的部分，其它部分不会点击

-------------->>>>>>>>>>>>>>  !!!!! 只要定位到了标签，并且那个标签在当前浏览器的窗口当中，就能点！！！！！！！
                               山禾 码云那个登陆按钮是定位到了，但窗口页面太小，登陆按钮没有在窗口当中，所以点不了，放大窗口之后就能点了

                             下拉滚动条的目的是为了加载异步数据，而不是为了看到相应的元素，只要没有异步数据，定位到标签就能进行相应的操作
                             就像这里可以直接定位到最后的提交按钮进行点击
'''

"""
第一次不准确代码如下
# for div in divs:
#     或许可以全部设置成点击三次，这样就不用单独把多选那出来了 
        --> 不行不行，看到效果才意识到随机数有可能随机到一样的数，这样的话最后可能选不到三个数
        ---> 亚你母🐮，只要定位到那个标签都能点到，只是我那一次运气不好，都点成前三个了，卧槽，仔细想想也是啊，每一个能够点击的a标签我都定位
            到了，所以每一个a标签都有可能被随机点击到啊 ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        
        
#     a_tags = div.find_elements(By.CSS_SELECTOR, 'li a')
#     # print(a_tags)
#     a_num = len(a_tags)
# 
#     i = 1
#     while i <= 3:
#         time.sleep(1)
#         a_tags[random.randint(0, a_num - 1)].click()  # random.randint(a, b)是闭区间
#         i += 1
# # print(a_num)
# 
# driver.find_element(By.CSS_SELECTOR, '.submitbutton').click()
"""
for div in divs:
    # target = driver.find_element(By.CSS_SELECTOR, "div")
    # driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

    a_tags = div.find_elements(By.CSS_SELECTOR, 'li a')
    a_tags_type = div.find_element(By.CSS_SELECTOR, 'li a').get_attribute('class')
    # print(a_tags_type)
    '''同一个变量有多个值的判断用elif'''
    if a_tags_type == 'jqRadio':
        time.sleep(1)
        a_tags[random.choice(range(len(a_tags)))].click()
    elif a_tags_type == 'jqCheckbox':
        new_array = random.sample(a_tags, 3)
        for i in new_array:
            time.sleep(1)
            i.click()

driver.find_element(By.CSS_SELECTOR, '.submitbutton').click()

time.sleep(2)

'''
网页中查看.rect-bottom这个的时候莫名奇妙会多一个没有这个class的元素，不用管，最终不会得到没有这个class值的那个元素
很多网页都有这种情况，只需要看多的那个标签有没有那个属性值，没有的话就不用管
'''
# driver.find_element(By.CSS_SELECTOR, '.rect-bottom').click()

input()

driver.close()
