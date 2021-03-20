import websockets
import asyncio
import json

data = '\0'

async def upbit_ws_client(coin):
    uri = "wss://api.upbit.com/websocket/v1"

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
            print('{}원 시간:{}\n'.format(str(data.get('tp')),str(data.get('ttm'))))
            # 손절 라인 가격이 되면 매도 

async def main(coin):
    await upbit_ws_client(coin)

def websocket_start(coin):
    asyncio.run(main(coin))