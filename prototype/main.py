from getnew import get_new_disclosure
from balance_check import get_balance
import upbit_websocket
from ML_disclosure import model
from buy_and_sell import upbit_buy, upbit_sell

access_key = 'mvkTaYkcAmtvhU0KUq8ZaFEoDEoxyxl2zL3Y4q2I'
secret_key = 'dLxGxfLbZcrtRLMKXPssbqrVIQbUyoFYMEHwBGdv'

while(1):
    # 새공시 가져오기
    disclosure = get_new_disclosure()

    idx = disclosure.find(']')
    coin = disclosure[1:idx]
    article = disclosure[idx+1:]

    # 호재 판단 머신러닝 모델
    expected_profit = model(coin, article)

    # KRW마켓에 있는 코인인지 확인하는 로직
    if (True):
        if (expected_profit > 10):
            # KRW 잔액 체크
            KRW_balance = get_balance(access_key, secret_key, 'KRW')

            # 시장가 풀매수
            upbit_buy(access_key, secret_key, coin, KRW_balance['balance'])

            # 매수한 코인 단가/수량 체크
            coin_balance = get_balance(access_key, secret_key, 'coin')

            # 지정가 매도 기대 단가 설정 (업비트 KRW 단위 참고하여 반올림하는 함수 필요)
            expected_price = ((1+(expected_profit/100)) * coin_balance['avg'])

            # 지정가 매도 주문
            upbit_sell(access_key, secret_key, coin, coin_balance['balance'], expected_price)

            # 매수한 코인 실시간 조회 + 손절 or 지정가 매도시 처음으로 돌아가서 새공시 가져오기
            upbit_websocket.websocket_start(coin) 






