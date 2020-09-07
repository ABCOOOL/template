from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
  "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
})

time.sleep(2)
# driver.get('https://www.toutiao.com/ch/news_hot/')
driver.get('https://www.chacewang.com/ProjectSearch/CopyIndex?searchText=5G')
