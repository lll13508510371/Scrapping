from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 浏览器配置选项功能

driver = webdriver.Chrome()

# 修改浏览器属性放置到实例化浏览器对象后面 window.navigator.webdriver
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => false
    })
  """
})
# 真实游览器当中是false ，模拟浏览器当中是true，所以需要修改为false

driver.get('https://qikan.cqvip.com/Qikan/Journal/JournalGuid?from=index')
print(driver.page_source)

input()

driver.quit()
"""
并不是所有的检测方式都是检测此浏览器属性, 如果说是根据js检测selenium,那么就需要js解密
这个属性添加了还是得不到数据就需要js逆向解密 与其用seleniumjs逆向解密，不如抓包js逆向解密，因为抓包js逆向解密会快很多
"""


"""
# selenium速度慢
启动浏览器
渲染页面(js页面）
"""