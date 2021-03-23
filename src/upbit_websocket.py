import websockets
import asyncio
import json
import upbit_trade
import checker_balance
import round_unit
import logger

async def upbit_ws_client(access_key, secret_key, coin, volume, price, expected_price, uuid):
    logger.write_system_log("Enter upbit ws client")
    uri = "wss://api.upbit.com/websocket/v1"

    stoploss_percentage = 0.08 #손절 라인 설정
    logger.write_system_log(f"Stoploss percentage : {stoploss_percentage}")

    stoploss_price = round_unit.round_price((1-stoploss_percentage) * float(price))

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

        logger.write_system_log("Check Coin Price")
        while True:
            data = await websocket.recv()
            data = json.loads(data)
            # print('{}원 시간:{}\n'.format(str(data.get('tp')),str(data.get('ttm'))))
            
            # 손절 라인 가격이 되면 지정가 매도 취소 후 시장가 매도하고 break
            if (stoploss_price == data.get('tp')):
                upbit_trade.sell_cancel(access_key, secret_key, uuid)
                upbit_trade.stoploss(access_key, secret_key, coin, volume)
                logger.write_trade_log("LOSS!!! SIBAL!!")
                break
            # 매도되면 break
            elif (data.get('tp') == expected_price):
                try:
                    if(checker_balance.get_balance(access_key, secret_key, coin)['balance'] == 0):
                        continue
                except:
                    logger.write_trade_log("PROFIT!!!!")
                    break

async def main(access_key, secret_key, coin, volume, price, expected_price, uuid):
    await upbit_ws_client(access_key, secret_key, coin, volume, price, expected_price, uuid)

def websocket_start(access_key, secret_key, coin, volume, price, expected_price, uuid):
    asyncio.run(main(access_key, secret_key, coin, volume, price, expected_price, uuid))