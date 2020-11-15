from selenium import webdriver
import time

# 去掉浏览器测试的小黄条
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
# option.add_argument('headless')

# 生成一个ChromeDriver
driver = webdriver.Chrome(options = option)
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('B站')
driver.find_element_by_id('su').click()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()