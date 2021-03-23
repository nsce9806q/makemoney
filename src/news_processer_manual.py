import logger

def model(coin, article):
    logger.write_system_log("Enter NPM - Manual")

    if ('기공개' in article) :
        return 10

    elif ('소각' in article) :
        return 0

    elif ('BUYING_TEST' in article) :
        logger.write_system_log("TEST PROFIT APPLIED")
        return 1

    else :
        return 24

# 호재 판단 ML 모델 완성도 부족시 
# 단계별 매도 주문으로 대체하고
# 특정 키워드가 있으면 매수를 하지 않게 끔 바꾼다 ('상장 폐지' 같은)