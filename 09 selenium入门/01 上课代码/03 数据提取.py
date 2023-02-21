import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能


driver = webdriver.Chrome()

driver.get('https://www.douban.com/')

# print(driver.page_source)
result1 = driver.find_element(By.ID, 'anony-reg-new')
print(result1)

result2 = driver.find_element(By.NAME, 'google-site-verification')
print(result2)


result3 = driver.find_element(By.CLASS_NAME, 'inp')
print(result3)

# 根据标签包含的文本内容获取标签(精确匹配) --> 因为精确匹配，估计只有一个，如果有两个应该会报错
result4 = driver.find_element(By.LINK_TEXT, '下载豆瓣 App')
print(result4)

# 根据标签包含的文本内容获取标签(模糊匹配)
result5 = driver.find_elements(By.PARTIAL_LINK_TEXT, '豆瓣')
print(result5)
print(len(result5))

# 根据标签的名字获取标签
result6 = driver.find_elements(By.TAG_NAME, 'div')
print(result6)
print(len(result6))
print('*' * 50)

"""
使用selenium内置方法css 或者xpath 定位标签的时候
只能使用定位功能, 不能使用属性提取或者取包含的文本内容

selenium中. css语法和xpath语法仅支持定位功能, 不支持属性提取或者取包含的文本内容
因为selenium中有方法可以属性提取或者取包含的文本内容
"""
# 根据xpath获取标签
result7 = driver.find_elements(By.XPATH, '//a[@class="lnk-app"]')
print(result7)

# 根据css选择器获取标签
result8 = driver.find_elements(By.CSS_SELECTOR, '.lnk-app')
print(result8)

input()  # 阻塞程序
driver.quit()


"""
parsel.Selector(driver.page_source)  
css  xpath

但是selenium, 有内置的数据提取方法
"""