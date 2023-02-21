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

ActionChains(driver).drag_and_drop(drag, drop).perform()

"""处理弹窗"""
alert = driver.switch_to.alert  # 切换弹窗
print(alert.text)
alert.accept()

input()
driver.quit()


