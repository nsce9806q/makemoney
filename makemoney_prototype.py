from selenium import webdriver
from selenium.webdriver.chrome.options import Options #열려 있는 크롬으로 제어
from time import sleep #대기 함수
from tqdm import tqdm
import pandas as pd

# CMD로 사전 실행
# cd C:/Program Files/Google/Chrome\Application //chrome.exe가 위치한 디렉토리
# chrome.exe --remote-debugging-port=9222 --user-data-dir=C:/ChromeTemp


# 새 기사
def get_new_disclosure():
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "./chromedriver.exe"
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)

    driver.get("https://upbit.com/service_center/disclosure")
    sleep(5) # 웹브라우저 보안 확인하는 동안 기다리기

    # 최근 마지막 공시 3개 저장
    disclosure_1 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[1]/td[1]/a')
    disclosure_2 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[2]/td[1]/a')
    disclosure_3 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[3]/td[1]/a')
    d1 = disclosure_1.text
    d2 = disclosure_2.text
    d3 = disclosure_3.text

    while(1):
        disclosure_new = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[1]/td[1]/a')
        disclosure = disclosure_new.text
        if (disclosure == d1):
            driver.refresh()
            sleep(10)
        else:
            if (disclosure != d2 and disclosure != d3):
                break
            else:
                sleep(10)
                driver.refresh()
    return(disclosure)

news = get_new_disclosure()
print(news)

# 공시에서 코인과 기사 제목 분리
def separate_coin_article (disclosure, coin_or_article):
    idx = disclosure.text.find(']')
    if (coin_or_article == 'c'):
        coin = disclosure.text[1:idx]
        return coin
    else:
        context = disclosure.text[idx+1:]
        return context


