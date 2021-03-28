from selenium import webdriver
from selenium.webdriver.chrome.options import Options #열려 있는 크롬으로 제어
from time import sleep #대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import *
from open_upbit_again import open_again

# 새 기사
def get_new_disclosure():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "./chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)

    driver.get("https://upbit.com/service_center/disclosure")
    sleep(20) # 웹브라우저 보안 확인하는 동안 기다리기

    # 최근 마지막 공시 3개 저장
    disclosure_1 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[1]/td[1]/a')
    disclosure_2 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[2]/td[1]/a')
    disclosure_3 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[3]/td[1]/a')
    d1 = disclosure_1.text
    d2 = disclosure_2.text
    d3 = disclosure_3.text

    # 새공시 뜰때까지 2~3초마다 무한 새로고침
    while(1):
        try: 
            disclosure_new = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[1]/td[1]/a')))
            # disclosure_new = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[1]/td[1]/a')
            disclosure = disclosure_new.text
            
            if (disclosure == d1):
                sleep(randint(2,3))
                driver.refresh()
            else:
                if (disclosure != d2 and disclosure != d3):
                    break
                else:
                    sleep(7)
                    driver.refresh()

        except:
            print("업비트 브라우저 재 로딩 필요")
            open_again()
            driver = webdriver.Chrome(chrome_driver, options=chrome_options)
            driver.get("https://upbit.com/service_center/disclosure")
    return(disclosure)