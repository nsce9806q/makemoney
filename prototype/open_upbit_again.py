import pyautogui as pag
from time import sleep, strftime, localtime, time

def open_again():
    pag.moveTo(270,30)
    sleep(1)
    pag.click()
    pag.moveTo(370,485)
    sleep(1)
    pag.click()
    pag.moveTo(230,25)
    sleep(1)
    pag.click()
    sleep(15)
    print(strftime('%y-%m-%d %H:%M:%S', localtime(time())))
    print("업비트 브라우저 재 로딩")