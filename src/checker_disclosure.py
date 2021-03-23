from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
from random import randint

import pyautogui as pag
import logger

# GETTER - New Disclosure
def get_newDisclosure():
    # Chrome
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "chromedriver.exe"
    
    # Driver
    driver = webdriver.Chrome(chrome_driver, options = chrome_options)

    # Go Upbit Web!
    driver.get("https://upbit.com/service_center/disclosure")

    # Wait 20 sec - Browser authentication
    sleep(20)

    # Save Recent 3 Disclosure
    disclosure_1 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[1]/td[1]/a').text
    disclosure_2 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[2]/td[1]/a').text
    disclosure_3 = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[3]/td[1]/a').text

    # Log - Recent 3 Disclosure
    logger.write_system_log(disclosure_1)
    logger.write_system_log(disclosure_2)
    logger.write_system_log(disclosure_3)

    # Refresh Web
    while (1) :
        try : 
            disclosure_new = driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[1]/td[1]/a')
            disclosure = disclosure_new.text
            
            if (disclosure == disclosure_1) :
                sleep(randint(5,8))
                driver.refresh()
                sleep(2)
            
            else :
                if (disclosure != disclosure_2 and disclosure != disclosure_3) :
                    break
                else :
                    sleep(7)
                    driver.refresh()
                    sleep(2)

        except :
            logger.write_system_log("Reload Chrome Brower")

            reload_upbit_web()
            driver = webdriver.Chrome(chrome_driver, options=chrome_options)
            driver.get("https://upbit.com/service_center/disclosure")

    return(disclosure)

def reload_upbit_web() :
    pag.moveTo(270,30)
    sleep(1)
    pag.click()
    
    pag.moveTo(370,485)
    sleep(1)
    pag.click()
    
    pag.moveTo(230,25)
    sleep(1)
    
    pag.click()
    sleep(20)

