from upbitAPI import Upbit_API 

access_key = 'mvkTaYkcAmtvhU0KUq8ZaFEoDEoxyxl2zL3Y4q2I'
secret_key = 'dLxGxfLbZcrtRLMKXPssbqrVIQbUyoFYMEHwBGdv'

while (True):
    a = Upbit_API(access_key, secret_key)
    
    # KRW 잔액 체크
    a.check_KRW()