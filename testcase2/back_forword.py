from time import sleep

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id('kw').send_keys("无敌")
driver.find_element_by_id('su').click()
sleep(2)
# 后退
driver.back()
sleep(2)
# 前进
driver.forward()
sleep(2)
# 刷新
driver.refresh()
sleep(2)
driver.quit()

