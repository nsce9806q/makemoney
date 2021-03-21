def round_price(price):
    if (price < 10):
        rounded_price = round(price, 2)
    elif (price < 100):
        rounded_price = round(price, 1)
    elif (price < 1000):
        rounded_price = round(price)
    elif (price < 10000):
        rounded_price = round(price) - round(price)%5
    elif (price < 100000):
        rounded_price = round(price) - round(price)%10
    elif (price < 500000):
        rounded_price = round(price) - round(price)%50
    elif (price < 1000000):
        rounded_price = round(price) - round(price)%100
    elif (price < 2000000):
        rounded_price = round(price) - round(price)%500
    else:
        rounded_price = round(price) - round(price)%1000
    
    return rounded_price