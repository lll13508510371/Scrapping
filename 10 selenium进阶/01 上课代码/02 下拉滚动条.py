from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://www.douban.com/')

# document.documentElement.scrollTop 指定滚动的高度
# document.documentElement.scrollHeight  获取当前页面的最大高度
js = 'document.documentElement.scrollTop=3000'
js_all = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'
driver.execute_script(js_all)

input()
driver.quit()


