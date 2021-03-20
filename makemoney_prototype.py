from selenium import webdriver
from selenium.webdriver.chrome.options import Options #열려 있는 크롬으로 제어
from time import sleep # 대기 함수
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import websockets
import asyncio
import json
import multiprocessing as mp
from PyQt5.QtCore import *

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("./makemoney_prototype_ui.ui")[0]

async def upbit_ws_client(q):
    uri = "wss://api.upbit.com/websocket/v1"

    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [
            {"ticket":"test"},
            {
                "type":"ticker",
                "codes":["KRW-XRP"],
                "isOnlyRealtime":True
            },
            {"format":"SIMPLE"}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            q.put(data)

async def main(q):
    await upbit_ws_client(q)

def producer(q):
    asyncio.run(main(q))

class Consumer(QThread):
    poped = pyqtSignal(dict)

    def __init__(self,q):
        super().__init__()
        self.q = q  
    
    def run(self):
        while True:
            if not self.q.empty():
                data = q.get()
                self.poped.emit(data)

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # self.consumer = Consumer(q)
        # self.consumer.poped.connect(self.print_data)     
        # self.consumer.start()   

        self.startbutton.clicked.connect(self.startfunction)

    @pyqtSlot()
    def judgement(self, profit_expected):
        if (profit_expected>5):
            self.text_ML.setPlainText("good news")
        else: 
            self.text_ML.setPlainText("bad news")
            #정지함수 넣기

    def coin_and_article(self, disclosure, option):
        idx = disclosure.find(']')
        if(option == 'c'):
            coin = disclosure[1:idx]
            return coin
        else:
            article = disclosure[idx+1:]
            return article

    def profit_expected_model(self, article):
        return 10

    # 새 기사
    def get_new_disclosure(self):
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
		
        # 새공시 뜰때까지 10초마다 무한 새로고침
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

    @pyqtSlot()
    def startfunction(self):
        self.text_status.setPlainText("시작!")
        disclosure = self.get_new_disclosure()
        self.text_newdisclosure.setPlainText(disclosure)
        profit_expected = self.profit_expected_model(coin_and_article(disclosure, 'a'))
        self.judgement(profit_expected)
        coin = 'c'

if __name__ == "__main__" :
    q = mp.Queue()
    p = mp.Process(name="Producer", target=producer, args=(q,), daemon=True)

    p.start()

    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 


    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


# CMD로 사전 실행
# cd C:/Program Files/Google/Chrome\Application //chrome.exe가 위치한 디렉토리
# chrome.exe --remote-debugging-port=9222 --user-data-dir=C:/ChromeTemp


