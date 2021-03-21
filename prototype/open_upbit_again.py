import pyautogui as pag
from time import sleep

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
    sleep(20)