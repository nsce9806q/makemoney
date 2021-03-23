from selenium import webdriver
from selenium.webdriver.chrome.options import Options #열려 있는 크롬으로 제어
from time import sleep #대기 함수
from tqdm import tqdm
import pandas as pd

#CMD로 사전 실행
#cd C:/Program Files/Google/Chrome\Application //chrome.exe가 위치한 디렉토리
#chrome.exe --remote-debugging-port=9222 --user-data-dir=C:/ChromeTemp


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = "./chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, options=chrome_options)

driver.get("https://upbit.com/service_center/disclosure")
sleep(10) #웹브라우저 보안 확인하는 동안 기다리기
print(driver.current_url)


for i in tqdm(range(40)):
    driver.find_element_by_xpath('//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/a').click() #더보기 버튼 클릭
    sleep(30)

columns = {
    '코인 명': [],
    '공시 명': [],
    '날짜': []
}
train = pd.DataFrame(columns)

for i in tqdm(range(1, 578)):
    article_path = '//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[{}]/td[1]/a'.format(i)
    date_path = '//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/div/div[2]/table/tbody/tr[{}]/td[2]'.format(i)
    article = driver.find_element_by_xpath(article_path)
    date = driver.find_element_by_xpath(date_path)
    # print(article.text, " ", date.text, sep='\n')

    idx = article.text.find(']')
    name = article.text[1:idx]
    context = article.text[idx+1:]

    new_data = {
        '코인 명': name,
        '공시 명': context,
        '날짜': date.text
    }
    train = train.append(new_data, ignore_index=True)

train.to_csv("train_data.csv")

print("FINISH")