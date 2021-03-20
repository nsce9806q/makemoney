from getnew import get_new_disclosure
from balance_check import get_balance
import upbit_websocket
from ML_disclosure import model
from buy_and_sell import *

access_key = 'mvkTaYkcAmtvhU0KUq8ZaFEoDEoxyxl2zL3Y4q2I'
secret_key = 'dLxGxfLbZcrtRLMKXPssbqrVIQbUyoFYMEHwBGdv'

while(1):
    # disclosure = get_new_disclosure()

    disclosure = '[DKA] 안녕안녕'

    idx = disclosure.find(']')
    coin = disclosure[1:idx]
    article = disclosure[idx+1:]

    expected_profit = model(coin, article)

    if (expected_profit > 10):
        # KRW 잔액 체크
        KRW_balance = get_balance(access_key, secret_key, 'KRW')
        


        # 시장가 풀매수
        upbit_buy(access_key, secret_key, coin, KRW_balance['balance'])

        # 매수한 코인 단가/수량 체크
        coin_balance = get_balance(access_key, secret_key, 'coin')

        # 지정가 매도 주문
        upbit_sell(access_key, secret_key, coin, coin_balance['price'], coin_balance['volume'])

        upbit_websocket.websocket_start(coin) 






