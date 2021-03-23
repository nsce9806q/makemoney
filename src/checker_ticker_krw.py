import pyupbit

def check_krw_tickers_pyupbit(coin) :
    krw_tickers = pyupbit.get_tickers(fiat="KRW")

    for i in range (len(krw_tickers)):
        krw_tickers[i] = krw_tickers[i].lstrip('KRW-')

    if (coin in krw_tickers):
        return True
    else: 
        return False

def check_krw_tickers(coin) :
    # 리스트 정확한걸로 수정 필요
    krw_tickers = ['MVL', 'BTT', 'NPXS', 'XRP', 'RFR', 'BTC', 'MED', 'MBL', 'STMX', 'CRE', 'META', 'IOST', 'CHZ', 'CRO', 'MFT', 'ETH', 'OBSR', 'SC', 'TT', 'HUNT', 'MOC', 'AHT', 'SPND', 'ORBS', 'XEM', 'SSX', 'IQ', 'DKA', 'AQT', 'QKC', 'PXL', 'XLM', 'BORA', 'ADA', 'EOS', 'TRX', 'TSHP', 'JST', 'LAMB', 'EDR', 'ANKR', 'IGNIS', 'PCI', 'UPP', 'MARO', 'MLK', 'HUM', 'STPT', 'SNT', 'HBAR', 'SAND', 'BCH', 'QTCON', 'VET', 'POLY', 'ENJ', 'DOT', 'TFUEL', 'AERGO', 'FCT2', 'DOGE', 'SOLVE', 'XTZ', 'LBC', 'WAXP', 'GLM', 'MANA', 'SXP', 'ICX', 'ZIL', 'PLA', 'NEO', 'TON', 'LTC', 'QTUM', 'THETA', 'STEEM', 'ARK', 'ONT', 'POWR', 'LSK', 'BTG', 'LOOM', 'BSV', 'SRN', 'GAS', 'IOTA', 'LINK', 'DMT', 'ELF', 'MTL', 'CBK', 'OMG', 'KAVA', 'ONG', 'ARDR', 'ZRX', 'HIVE', 'SBD', 'CVC', 'GRS', 'BAT', 'SRM', 'KMD', 'ATOM', 'EMC2', 'STORJ', 'BCHA', 'REP', 'WAVES', 'STRAX', 'KNC']

    if (coin in krw_tickers):
        return True
    else: 
        return False