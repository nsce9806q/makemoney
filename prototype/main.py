from getnew import get_new_disclosure
import upbit_websocket

coin = 'XRP'

upbit_websocket.websocket_start(coin)

while(1):
    print(upbit_websocket.data)


