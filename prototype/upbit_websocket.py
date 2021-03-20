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

async def main(coin):
    await upbit_ws_client(coin)

def websocket_start(coin):
    asyncio.run(main(coin))