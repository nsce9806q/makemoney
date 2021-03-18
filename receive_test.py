import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import websockets
import asyncio
import json
import multiprocessing as mp
from PyQt5.QtCore import *
import time

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("./recieve_test.ui")[0]

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

        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.print_data)     
        self.consumer.start()   

        self.status_window.setPlainText("Test")

    def print_data(self, data):
        self.log_window.append("{}원".format(str(data.get('tp'))))

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