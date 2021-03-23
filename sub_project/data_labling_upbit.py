import pandas as pd
import requests
import json
from tqdm import tqdm

url = "https://api.upbit.com/v1/candles/days"

original = pd.read_csv('./disclosure.csv')

columns = {
    '코인 명': [],
    '공시 명': [],
    '날짜': [],
    '마켓': [],
    '전일 종가': [],
    '최저가': [],
    '최고가': [],
    'BTC 상승률': [],
    '상승률': []
}
dataset = pd.DataFrame(columns)

for i in tqdm(range(0, 577)):
    coin = original.iloc[i]['코인 명']
    coin_KRW = 'KRW-{}'.format(coin)
    date = '{}T23:59:59Z'.format(original.iloc[i]['날짜'].replace('.','-'))

    # KRW 마켓 조회
    querystring = {"market":coin_KRW,"to":date,"count":"1","convertingPriceUnit":"KRW"}
    response = requests.request("GET", url, params=querystring)

    # KRW 비상장 코인일 경우 BTC 마켓으로 재조회
    if (response.status_code != 200 or response.text == '[]'):
        coin_BTC = "BTC-{}".format(coin)
        querystring = {"market":coin_BTC,"to":date,"count":"3","convertingPriceUnit":"KRW"}
        response = requests.request("GET", url, params=querystring)
    
    BTCstring = {"market":'KRW-BTC',"to":date,"count":"3"}
    BTC_response = requests.request("GET", url, params=BTCstring)
    BTC_change = BTC_response.json()[0]['change_rate']

    if (response.status_code == 200):
        new_data = {
            '코인 명': original.iloc[i]['코인 명'],
            '공시 명': original.iloc[i]['공시 명'],
            '날짜': original.iloc[i]['날짜'],
            '마켓': response.json()[0]['market'][:3],
            '전일 종가': response.json()[0]['prev_closing_price'],
            '최저가': response.json()[0]['low_price'],
            '최고가': response.json()[0]['high_price'],
            'BTC 상승률': "{}%".format(round(BTC_change*100,2)),
            '상승률': "{}%".format(round(((response.json()[0]['high_price']/response.json()[0]['prev_closing_price'])-1)*100,2))
        }
        dataset = dataset.append(new_data, ignore_index=True)

dataset.to_csv('disclosure_price.csv')

print("FINISH")