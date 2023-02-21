from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')


# 新开一个窗口，通过执行js来新开一个窗口
js = 'window.open("https://www.sogou.com");'
driver.execute_script(js)


input()
driver.quit()

# selenium开发出来最开始不是用于爬虫, 是用来做网页测试

'''
！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
虽然说是模拟浏览器请求，但有些js加密数据是得不到的，该用js解密还得用 
所以有些时候网页渲染的内容（elements）和得到的内容是不一样的，根据page_source得到的结果为准

'''
