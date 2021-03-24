import checker_disclosure
import checker_ticker_krw
import logger
import checker_balance
import time
import round_unit

# Upbit
import upbit_trade
import upbit_websocket

# News judgment model
import news_processer_ml
import news_processer_manual

# Static
ML_MODEL_ENABLE = False

# Params
access_key = ''
secret_key = ''

# Write Initial Log
logger.write_system_log("#### START SYSTEM ####")
logger.write_system_log(f"ML_MODEL_ENABLE\t: {ML_MODEL_ENABLE}")
logger.write_system_log(f"KRW_BALANCE\t: {checker_balance.get_balance(access_key, secret_key, 'KRW')}")

# Start Main While Loop
while (True) :
    # Log
    logger.write_system_log("main.py\tMain While Loop - Start")
    time.sleep(10)

    # Check New Disclosure
    disclosure = checker_disclosure.get_newDisclosure()

    # Print Log - new Disclosure
    logger.write_system_log(f"New Disclosure!\t: {disclosure}")

    # Split Disclosure String
    idx = disclosure.find(']')
    coin = disclosure[1:idx]
    article = disclosure[idx+1:]

    # ML Model
    if (ML_MODEL_ENABLE == True) :
        expected_profit = news_processer_ml.model(coin, article)
    else :
        expected_profit = news_processer_manual.model(coin, article)

    # Check KRW Market
    if (checker_ticker_krw.check_krw_tickers(coin)):
        if (expected_profit > 0):
            logger.write_trade_log("#### TRADING START ####")
            logger.write_trade_log(f"COIN_NAME\t\t: {coin}")

            # Check My KRW Balance
            my_krw_balance = checker_balance.get_balance(access_key, secret_key, 'KRW')
            logger.write_trade_log(f"MY_KRW_BALANCE\t: {my_krw_balance}")

            # 시장가 풀매수
            upbit_trade.buy_market_price(access_key, secret_key, coin, str(float(my_krw_balance['balance'])-2000))
            time.sleep(1)

            # 매수한 코인 단가/수량 체크
            my_coin_balance = checker_balance.get_balance(access_key, secret_key, coin)
            volume = my_coin_balance['balance'] #코인 수량
            price = my_coin_balance['avg'] #평균 단가

            # 지정가 매도 기대 단가 설정 
            expected_price = round_unit.round_price(((1+(expected_profit/100)) * float(price)))

            # 지정가 매도 주문
            profit_sell = upbit_trade.sell_specified_price(access_key, secret_key, coin, expected_price, volume)

            # 매수한 코인 실시간 조회 + 손절 or 지정가 매도시 다시 루프
            upbit_websocket.websocket_start(access_key, secret_key, coin, volume, price, expected_price, profit_sell['uuid']) 

    t = 0