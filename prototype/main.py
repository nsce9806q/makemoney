from getnew import get_new_disclosure
from balance_check import get_balance
import upbit_websocket
from ML_disclosure import model
from buy_and_sell import upbit_buy, upbit_sell
from KRWtickers import check_KRWtickers
from round_unit import round_price
from time import sleep, strftime, localtime, time

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']

while (True):
     # KRW 잔액 체크
    KRW_balance = get_balance(access_key, secret_key, 'KRW')

    # 새공시 가져오기
    disclosure = get_new_disclosure()
    print(disclosure)
    print(strftime('%y-%m-%d %H:%M:%S', localtime(time())))

    # 공시 문자열 나누기
    idx = disclosure.find(']')
    coin = disclosure[1:idx]
    article = disclosure[idx+1:]

    # 호재 판단 머신러닝 모델
    expected_profit = model(coin, article)

    # KRW마켓에 있는 코인인지 확인하는 로직
    if (check_KRWtickers(coin)):
        if (expected_profit > 0):
           
            # 시장가 풀매수
            print(strftime('%y-%m-%d %H:%M:%S', localtime(time())))
            upbit_buy(access_key, secret_key, coin, str(float(KRW_balance['balance'])-2000))

            sleep(15)

            # 매수한 코인 단가/수량 체크
            print(strftime('%y-%m-%d %H:%M:%S', localtime(time())))
            coin_balance = get_balance(access_key, secret_key, coin)
            volume = coin_balance['balance'] #코인 수량
            price = coin_balance['avg'] #평균 단가

            # 지정가 매도 기대 단가 설정 
            expected_price = round_price(((1+(expected_profit/100)) * float(price)))

            # 지정가 매도 주문
            print(strftime('%y-%m-%d %H:%M:%S', localtime(time())))
            profit_sell = upbit_sell(access_key, secret_key, coin, expected_price, volume)
            

            # 매수한 코인 실시간 조회 + 손절 or 지정가 매도시 다시 루프
            print(strftime('%y-%m-%d %H:%M:%S', localtime(time())))
            upbit_websocket.websocket_start(access_key, secret_key, coin, volume, price, expected_price, profit_sell['uuid']) 

    t = 0




