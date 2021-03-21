import pyupbit

def check_KRWtickers(coin):
    KRW_tickers = pyupbit.get_tickers(fiat="KRW")

    for i in range (len(KRW_tickers)):
        KRW_tickers[i] = KRW_tickers[i].lstrip('KRW-')

    if (coin in KRW_tickers):
        return True
    else: 
        return False