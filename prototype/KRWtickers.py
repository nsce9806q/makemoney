def check_KRWtickers(coin):
    # 리스트 정확한걸로 수정 필요
    KRW_tickers = ['MVL', 'BTT', 'NPXS', 'XRP', 'RFR', 'BTC', 'MED', 'MBL', 'STMX', 'CRE', 'META', 'IOST', 'CHZ', 'CRO', 'MFT', 'ETH', 'OBSR', 'SC', 'TT', 'HUNT', 'MOC', 'AHT', 'SPND', 'ORBS', 'XEM', 'SSX', 'IQ', 'DKA', 'AQT', 'QKC', 'PXL', 'XLM', 'BORA', 'ADA', 'EOS', 'TRX', 'TSHP', 'JST', 'LAMB', 'EDR', 'ANKR', 'IGNIS', 'PCI', 'UPP', 'MARO', 'MLK', 'HUM', 'STPT', 'SNT', 'HBAR', 'SAND', 'BCH', 'QTCON', 'VET', 'POLY', 'ENJ', 'DOT', 'TFUEL', 'AERGO', 'FCT2', 'DOGE', 'SOLVE', 'XTZ', 'LBC', 'WAXP', 'GLM', 'MANA', 'SXP', 'ICX', 'ZIL', 'PLA', 'NEO', 'TON', 'LTC', 'QTUM', 'THETA', 'STEEM', 'ARK', 'ONT', 'POWR', 'LSK', 'BTG', 'LOOM', 'BSV', 'SRN', 'GAS', 'IOTA', 'LINK', 'DMT', 'ELF', 'MTL', 'CBK', 'OMG', 'KAVA', 'ONG', 'ARDR', 'ZRX', 'HIVE', 'SBD', 'CVC', 'GRS', 'BAT', 'SRM', 'KMD', 'ATOM', 'EMC2', 'STORJ', 'BCHA', 'REP', 'WAVES', 'STRAX', 'KNC']

    if (coin in KRW_tickers):
        return True
    else: 
        return False