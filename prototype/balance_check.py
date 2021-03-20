import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode

import requests



def get_balance(access_key, secret_key, coin):
    server_url = 'https://api.upbit.com'

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)

    data = res.json()

    for i in range(len(data)):
        if (data[i]['currency'] == coin):
            balance = data[i]['balance']
            avg = data[i]['avg_buy_price']
            balance_info = {'balance': balance, 'avg': avg}
            return balance_info
             
balance_info = get_balance(access_key, secret_key, 'DKA')


