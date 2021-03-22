def model(coin, article):
    if('기공개' in article):
        return 10
    elif ('소각' in article):
        return 0
    else:
    	return 25 #목표 이익률

# 호재 판단 ML 모델 완성도 부족시 
# 단계별 매도 주문으로 대체하고
# 특정 키워드가 있으면 매수를 하지 않게 끔 바꾼다 ('상장 폐지' 같은)