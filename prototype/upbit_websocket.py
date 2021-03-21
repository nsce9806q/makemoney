import websockets
import asyncio
import json
from buy_and_sell import sell_cancel, stoploss
from balance_check import get_balance
from round_unit import round_price

async def upbit_ws_client(access_key, secret_key, coin, volume, price, expected_price, uuid):
    uri = "wss://api.upbit.com/websocket/v1"

    stoploss_percentage = 0.002 #손절 라인 설정
    stoploss_price = rounded_price((1-stoploss_percentage) * price)

    async with websockets.connect(uri) as websocket:
        subscribe_fmt = [
            {"ticket":"test"},
            {
                "type":"ticker",
                "codes":["KRW-{}".format(coin)], # 마켓 선택
                "isOnlyRealtime":True
            },
            {"format":"SIMPLE"}
        ]
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            # print('{}원 시간:{}\n'.format(str(data.get('tp')),str(data.get('ttm'))))
            
            # 손절 라인 가격이 되면 지정가 매도 취소 후 시장가 매도하고 break
            if (stoploss_price == data.get('tp')):
                sell_cancel(access_key, secret_key, uuid)
                stoploss(access_key, secret_key, coin, volume)
                break
            # 매도되면 break
            elif (data.get('tp') == expected_price):
                if(get_balance(access_key, secret_key, coin)['balance'] == 0):
                    break
            
            

async def main(access_key, secret_key, coin, volume, price, expected_price, uuid):
    await upbit_ws_client(access_key, secret_key, coin, volume, price, expected_price, uuid)

def websocket_start(access_key, secret_key, coin, volume, price, expected_price, uuid):
    asyncio.run(main(access_key, secret_key, coin, volume, price, expected_price, uuid))