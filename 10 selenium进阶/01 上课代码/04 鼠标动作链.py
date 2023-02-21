from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains  # 导入动作链功能

driver = webdriver.Chrome()

driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

# 进入到嵌套网页
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, '#iframeResult'))

# 找可以拖动的标签
drag = driver.find_element(By.CSS_SELECTOR, '#draggable')

# 找可以放置的标签
drop = driver.find_element(By.CSS_SELECTOR, '#droppable')

"""动作链拖动"""
# # 实例化一个动作链对象, 括号内部需要传递当前driver浏览器对象
# action = ActionChains(driver)
#
# # 定义一个鼠标动作
# action.drag_and_drop(drag, drop)
#
# # 执行动作
# action.perform()

# 支持链式调用
ActionChains(driver).drag_and_drop(drag, drop).perform()

input()
driver.quit()


