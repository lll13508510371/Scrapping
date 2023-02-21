import time
from selenium import webdriver
from selenium.webdriver.common.by import By  # 导入定位器功能
from selenium.webdriver.support.select import Select  # 导入下拉框处理功能


driver = webdriver.Chrome()
driver.get('https://www.jq22.com/demo/shengshiliandong/')

element = driver.find_element(By.CSS_SELECTOR, '#s_province')

# 实例化 select 对象, 括号内部传递获取到下拉框标签对象
select = Select(element)

"""选择下拉框内容"""
# 根据索引取下拉框, 从1开始
select.select_by_index(1)
time.sleep(3)

select.select_by_value('重庆市')
time.sleep(3)

select.select_by_visible_text('内蒙古')
time.sleep(3)


input()  # 阻塞程序
driver.quit()
