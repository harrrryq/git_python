#import sys
#import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import datetime
import time

def go():

	driver.get("https://clinic.smiley-reserve.jp/oji-kids/")
	driver.find_element_by_name('email').send_keys('username')
	driver.find_element_by_name('password').send_keys('password')
	driver.find_element_by_xpath('//*[@id="login_content"]/ul/li/input').click()
	driver.find_element_by_xpath('//*[@id="content_bar"]/div[1]/ul/li[1]/a').click()
	driver.find_element_by_xpath('//*[@id="reserve"]/table/tbody/tr[3]/td/a').click()
	driver.find_element_by_xpath('//*[@id="reserve"]/table/tbody/tr[2]/td[1]/a').click()
	driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/a[2]').click()

### logic body

driver = webdriver.Chrome(executable_path='/Users/yilin1116/Downloads/chromedriver')
go()

for i in range(120):
	driver.refresh()
	now_time = datetime.datetime.now()
	s_date = driver.find_element_by_xpath('//*[@id="calendar"]/table/tbody/tr[6]/td[2]/div[2]/div/span[2]')
	a = "print(s_date.text)"
	b = "未受付"
	music = '/System/Applications/Music.app'
	
	if a == b:
		print("*******************")
		print(s_date.text)
		print(now_time)
		print("*******************\n")
		#driver.get_screenshot_as_file("/Users/yilin1116/Desktop/yoyaku.png")
		time.sleep(10)


	else:
		print("*******Congrats!************")
		print(s_date.text)
		print(now_time)
		print("****************************\n")
		driver.get_screenshot_as_file("/Users/yilin1116/Desktop/yoyaku.png")
		break
		driver.close()

print(">>>>>>Finish<<<<<<")
