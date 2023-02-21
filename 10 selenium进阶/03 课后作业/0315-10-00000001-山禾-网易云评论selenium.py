"""
目标网址:https://music.163.com/#/playlist?id=924680166

要求:
	1. 使用selenium
	2. 爬取前面5页的评论数据保存为txt文件

"""
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def parse_data():
    comments = driver.find_elements(By.CSS_SELECTOR, '.itm')

    for comment in comments:
        total_comment_data = comment.find_element(By.CSS_SELECTOR, '.cnt.f-brk').text  # 包含了评论者名字的评论
        # print(total_comment_data)
        #     print(type(comment))
        '''
        ！！！！！！！！！！这里面正则表达式的内容冒号'：'是中文冒号，字符串的符号不能打成英文，是什么符号就输入什么符号
                        惯性思维，编写代码习惯性使用英文字符，这里一定要注意 ！！！！！！！！！！！！！！！！！！！！
        '''
        comment_data = re.findall('.*?：(.*)', total_comment_data)[0]  # 正则提取去除评论者名字的评论
        print(comment_data)
        with open('网易云.txt', mode='a', encoding='utf-8') as f:
            f.write(comment_data + '\n')


def click_next():
    next_tag = driver.find_element(By.LINK_TEXT, '下一页')
    next_tag.click()
    # js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    # driver.execute_script(js_all)


def scroll():
    # js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
    for i in range(1, 9, 2):
        time.sleep(0.5)
        j = i / 7
        js_all = f'document.documentElement.scrollTop = document.documentElement.scrollHeight*{j}'
        driver.execute_script(js_all)


if __name__ == '__main__':
    driver = webdriver.Chrome()

    driver.get('https://music.163.com/#/playlist?id=924680166')

    driver.implicitly_wait(10)

    # driver.maximize_window()

    comment_iframe = driver.find_element(By.CSS_SELECTOR, '#g_iframe')

    # print(type(comment_iframe))  -->  <class 'selenium.webdriver.remote.webelement.WebElement'>
    '''
    ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
    应该是下面分析的这样哈，反正不管怎么样，知道  这些标签在嵌套html当中  那就先切换了再进行滚动就不会错

    嵌套html和外层html都有自己的坐标轴位置，这里下一页点击的坐标轴位置是嵌套html的，所以要切换到嵌套html再滚动下拉条才能得到下一页按钮的坐标轴
    如果先滚动，再切换到嵌套html，是根据外层html的坐标轴位置定位，点击的位置就是其它的标签了
    --->selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <iframe name="contentFrame" id="g_iframe" class="g-iframe" scrolling="auto" frameborder="0" src="about:blank" allowfullscreen="true" cd_frame_id_="6b076408e3971083f07dce30a8baff7a"></iframe> is not clickable at point (1318, 1178). Other element would receive the click: <div class="hand" title="展开播放条"></div>
        selenium.common.exceptions.ElementClickInterceptedException：消息：元素点击被拦截：元素 <iframe name="contentFrame" id="g_iframe" class="g-iframe" scrolling="auto" frameborder="0" src="about:blank " allowfullscreen="true" cd_frame_id_="6b076408e3971083f07dce30a8baff7a"><iframe> 
        在点 (1318, 1178) 不可点击。其他元素将收到点击：<div class="hand" title="展开播放放条"><div>
    '''
    driver.switch_to.frame(comment_iframe)

    '''
    scroll() 这里没有异步加载的数据，所以不需要这样慢慢滑动等待数据加载的逻辑，直接一步滑到底就OK
    '''
    # scroll()
    '''这题必须要下拉，定位到下一页标签selenium定位到的坐标轴会展开播放条覆盖下一页按钮'''
    js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'  # 这个是从页面顶部开始下拉
    driver.execute_script(js_all)

    for i in range(1, 6):
        time.sleep(1)
        print(f'---------------------第{i}页评论---------------------' + '\n')
        parse_data()

        if i == 5:
            break

        click_next()
        time.sleep(1)
    '''
    这个网页只需要一次下拉，之后就是解析保存和翻页
    '''

    # input() #程序写完不需要阻塞看过程了

    driver.quit()

    '''
    ！！！！！！！！！！！！！！！！！！！！！！！可以用正则表达式只提取评论不提取名字！！！！！！！！！！！！！！！！！！！！！！！！！
    '''

    # scroll()

    # comment_iframe = driver.find_element(By.CSS_SELECTOR, '#g_iframe')
    #
    # driver.switch_to.frame(comment_iframe)
    #
    # # print(driver.page_source)
    #
    #
    #  # scroll()
    #  # driver.find_element(By.CSS_SELECTOR, '.zpgi.zpg2.js-i-1675909321180').click()
    #
    # # parse_data()
    # comments = driver.find_elements(By.CSS_SELECTOR, '.itm')
    #
    # for comment in comments:
    #     comment_data = comment.find_element(By.CSS_SELECTOR, '.cnt.f-brk').text
    #     print(comment_data)
    #     #     print(type(comment))
    #     with open('网易云.txt', mode='a', encoding='utf-8') as f:
    #         f.write(comment_data + '\n')
    #
    #
    #     # if i == 5:
    #     #     break
    #     # click_next(i + 1)
    # driver.find_element(By.LINK_TEXT, '下一页').click()
    #
    # input()
    #
    # driver.quit()
