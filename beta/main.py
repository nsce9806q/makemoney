from upbitAPI import Upbit_API 

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']

while (True):
    a = Upbit_API(access_key, secret_key)
    
    # KRW 잔액 체크
    a.check_KRW()
