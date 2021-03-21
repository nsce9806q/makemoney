import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests

server_url = 'https://api.upbit.com' 

# 시장가 매수
def upbit_buy(access_key, secret_key, coin, balance):
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

    print(res.json())
    return res.json()

# 지정가 매도
def upbit_sell(access_key, secret_key, coin, price, volume):
    
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

    return res.json()

# 손절 ㅠㅠ
def stoploss(access_key, secret_key, coin, volume):
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

    return res.json()

# 매도 취소
def sell_cancel(access_key, secret_key, uuid):
    query = {
        'uuid': uuid,
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

    return(res.json())