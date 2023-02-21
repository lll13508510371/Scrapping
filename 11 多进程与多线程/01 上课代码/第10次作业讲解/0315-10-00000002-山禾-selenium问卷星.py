import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

driver.get('https://www.wjx.cn/jq/87910206.aspx')
driver.implicitly_wait(10)

divs = driver.find_elements(By.CSS_SELECTOR, '.div_question')
print(divs)
print(len(divs))
"""
单选题: 1 - 10 列表中的索引范围是 0 - 9
多选题: 11 - 12 列表中的索引范围是 10 - 11
"""
one_choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
any_choice = [10, 11]

# 单选题
for i in one_choice:
    lis = divs[i].find_elements(By.CSS_SELECTOR, 'ul li')
    # 随机选取一个
    random.choice(lis).click()

# 多选题
for j in any_choice:
    lis = divs[j].find_elements(By.CSS_SELECTOR, 'ul li')
    # 随机选取三个
    # choices 可以随机选择多个, 有可能会重复
    # random.choices(lis).click()
    obj = random.sample(lis, k=3)
    for k in obj:
        k.click()


# 点击提交
driver.find_element(By.CSS_SELECTOR, '.submitbutton').click()
time.sleep(2)
# 点击智能认证
driver.find_element(By.CSS_SELECTOR, '.sm-ico .sm-ico-wave').click()


input()
driver.quit()
