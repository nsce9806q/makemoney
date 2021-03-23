import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests
import logger

server_url = 'https://api.upbit.com' 

# 시장가 매수
def buy_market_price(access_key, secret_key, coin, balance):
    logger.write_trade_log("TRADE : Buy Market Price Func")
    logger.write_trade_log(f"\tCOIN\t: {coin}")
    logger.write_trade_log(f"\tBALANCE\t: {balance}KRW")

    query = {
        'market': 'KRW-{}'.format(coin),
        'side': 'bid',
        # 'volume': '0.01',
        'price': balance,
        'ord_type': 'price'
    }

    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)

    logger.write_trade_log(f"\tRES\t: {res}")
    return res.json()


# 지정가 매도
def sell_specified_price(access_key, secret_key, coin, price, volume):
    logger.write_trade_log("TRADE : Sell Specified Price")
    logger.write_trade_log(f"\tCOIN\t: {coin}")
    logger.write_trade_log(f"\tPRICE\t: {price}KRW")
    logger.write_trade_log(f"\tBALANCE\t: {volume}{coin}")
    
    query = {
        'market': 'KRW-{}'.format(coin),
        'side': 'ask',
        'volume': volume,
        'price': price,
        'ord_type': 'limit'
    }

    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)

    logger.write_trade_log(f"\tRES\t: {res}")
    return res.json()


# 매도 취소
def sell_cancel(access_key, secret_key, uuid_code):
    logger.write_trade_log("TRADE : Sell Cancel")

    query = {
        'uuid': uuid_code,
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.delete(server_url + "/v1/order", params=query, headers=headers)

    logger.write_trade_log(f"\tRES\t: {res}")
    return(res.json())


# 손절 ㅠㅠ
def stoploss(access_key, secret_key, coin, volume):
    logger.write_trade_log("TRADE : Stop loss")

    query = {
        'market': 'KRW-{}'.format(coin),
        'side': 'ask',
        'volume': volume,
        'ord_type': 'market'
    }

    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
    logger.write_trade_log(f"\tRES\t: {res}")

    return res.json()

