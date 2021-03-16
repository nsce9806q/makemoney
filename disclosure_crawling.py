from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)


driver.get("https://upbit.com/service_center/disclosure")
sleep(10) #웹브라우스 보안 확인하는 동안 기다리기
print(driver.current_url)

driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/a').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/a').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/a').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/a').click()