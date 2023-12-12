import time
import json
#morning start me green ki body red k half se jyada krni h and hammer me hammer k baad wale ki body jyada krni h
# def check():
#     f2=list(data.values())[1]
#     with open('cndl.json', 'r+') as file:
#         data = json.load(file)
#     #print(data.keys())
#     #print(list(data.values())[0])
#     f1=list(data.values())[0]
#     f3=list(data.values())[2]
    #start_matching
    #print(f1,f2['start'],f3['end'])
def is_body(_data,n,b):
    candle=list(_data.values())[n]
    max_price = float(candle['max'])
    min_price = float(candle['min'])
    start_price = float(candle['start'])
    end_price = float(candle['end'])
    price_diff = max_price - min_price
    if ((abs(start_price-end_price)*100)/(price_diff)) >= b:
        return True
def is_green(_data,n):
        candle=list(_data.values())[n]
        start_price = float(candle['start'])
        end_price = float(candle['end'])
        if start_price<end_price:
            return True    
def is_red(_data,n):
        candle=list(_data.values())[n]
        start_price = float(candle['start'])
        end_price = float(candle['end'])
        if start_price>end_price:
            return True 



# downtrend to uptrend +==> buy
# Hammer, inverted hammer
def is_hammer(_data,n):
    candle=list(_data.values())[n]
    max_price = float(candle['max'])
    min_price = float(candle['min'])
    start_price = float(candle['start'])
    end_price = float(candle['end'])
    # price_diff = max_price - min_price
    body_size = abs(start_price - end_price)
    lower_shadow_size = abs(min_price - min(start_price, end_price))
    upper_shadow_size = abs(max(start_price, end_price) - max_price)
    if ((upper_shadow_size)>(2*body_size)) or ((lower_shadow_size) > (2 * body_size)) :
      return True
    else:
      return False

# morning star
def is_morning_star(candle1, candle2, candle3,candle4):
   # Check if candle1 is a long red candle
   if float(candle1['start']) > float(candle1['end']):
       # Check if candle2 is a small or doji green candle
       if (abs(float(candle2['start']) - float(candle2['end']))) <((float(candle2['max']) - float(candle2['min'])) * 0.15):
           # Check if candle3 is a long green candle
           if float(candle3['start']) < float(candle3['end']):
               if float(candle4['start']) < float(candle4['end']):
                # Check if the closing price of the third float(candlestick is above the middle of the first float(candlestick
                if float(candle3['end']) > ((float(candle1['start']) + float(candle1['end'])) / 2):
                    return True
   return False


# bullish engulfing
# piercing line ,, bullish abandoned baby

# uptrend to downtrend +==> sell
# shooting star
def is_shooting_star(_data,n):
    candle=list(_data.values())[n]
    max_price = float(candle['max'])
    min_price = float(candle['min'])
    start_price = float(candle['start'])
    end_price = float(candle['end'])
    price_diff = max_price - min_price
    body_size = abs(start_price - end_price)
    lower_shadow_size = abs(min_price - min(start_price, end_price))
    # upper_shadow_size = abs(max(start_price, end_price) - max_price)
    if ((body_size/price_diff)*100 < 10 ) and ((lower_shadow_size/price_diff)*100 < 12):
        return True
    else:
        return False
    
# hanging man
def is_hanging_man(_data,n):
    candle=list(_data.values())[n]
    max_price = float(candle['max'])
    min_price = float(candle['min'])
    start_price = float(candle['start'])
    end_price = float(candle['end'])
    price_diff = max_price - min_price
    body_size = abs(start_price - end_price)
    # lower_shadow_size = abs(min_price - min(start_price, end_price))
    upper_shadow_size = abs(max(start_price, end_price) - max_price)
    if ((body_size/price_diff)*100 < 10 ) and ((upper_shadow_size/price_diff)*100 < 12):
        return True
    else:
        return False
# bearish engulfing
# evening star
def is_evening_star(candle1, candle2, candle3,candle4):
   # Check if the first candlestick is green
   if float(candle1['start']) < float(candle1['end']) :
       # Check if the second (candlestick is small
       if (abs(float(candle2['start']) - float(candle2['end']))) < ((float(candle2['max']) - float(candle2['min'])) * 0.1):
           # Check if the third (candlestick is red
           if float(candle3['start']) > float(candle3['end']):
               if float(candle4['start']) > float(candle4['end']):
               # Check if the closing price of the third (candlestick is below the middle of the first (candlestick
                    if float(candle3['end']) < ((float(candle1['start']) + float(candle1['end'])) / 2):
                        return True
   return False

# dark cloud cover
# three black cover
#

























def is_dozi(_data,n):
        candle=list(_data.values())[n]
        max_price = float(candle['max'])
        min_price = float(candle['min'])
        start_price = float(candle['start'])
        end_price = float(candle['end'])
        price_diff = max_price - min_price
        if ((abs(start_price-end_price)) <=( 0.05 * price_diff)):
            return True
        else:
            return False
      



def printer(_data):
    for i in range(0,3):
        candle=list(_data.values())[i]
        max_price = float(candle['max'])
        min_price = float(candle['min'])
        start_price = float(candle['start'])
        end_price = float(candle['end'])
        price_diff = max_price - min_price
        print(i,"upper:",((max_price-max(start_price,end_price))*100)/price_diff,    "body :",((abs(start_price-end_price))*100)/price_diff,"lower:",((min(start_price,end_price)-min_price)*100)/price_diff)
    # print(list(current.items())[0][0], ":", "upper :" ,"body :" ,"lower :")
    
    #   ,sc[0], ":", "upper :" ,(sc[0]['max']-max(sc[0]['start'],sc[0]['end']))*100/sc[0]['max']-sc[0]['min'], sc[0],"body :",(abs(sc[0]['start']-sc[0]['end'])*100/sc[0]['max']-sc[0]['min']) ,"lower :", (min(sc[0]['start'],sc[0]['end'])-sc[0]['min'])*100/sc[0]['max']-sc[0]['min'],sc[1], ":", "upper :" ,(sc[1]['max']-max(sc[1]['start'],sc[1]['end']))*100/sc[1]['max']-sc[1]['min'], sc[1],"body :",(abs(sc[1]['start']-sc[1]['end'])*100/sc[1]['max']-sc[1]['min']) ,"lower :", (min(sc[0]['start'],sc[0]['end'])-sc[0]['min'])*100/sc[0]['max']-sc[0]['min'],sc[2], ":", "upper :" ,(sc[1]['max']-max(sc[2]['start'],sc[2]['end']))*100/sc[2]['max']-sc[2]['min'], sc[2],"body :",(abs(sc[2]['start']-sc[2]['end'])*100/sc[2]['max']-sc[2]['min']) ,"lower :", (min(sc[0]['start'],sc[0]['end'])-sc[0]['min'])*100/sc[0]['max']-sc[0]['min'])


    # print(sc[0], ":", "upper :" ,(sc[0]['max']-max(sc[0]['start'],sc[0]['end']))*100/sc[0]['max']-sc[0]['min'], sc[0],"body :",(abs(sc[0]['start']-sc[0]['end'])*100/sc[0]['max']-sc[0]['min']) ,"lower :", (min(sc[0]['start'],sc[0]['end'])-sc[0]['min'])*100/sc[0]['max']-sc[0]['min'])
    # print(sc[1], ":", "upper :" ,(sc[1]['max']-max(sc[1]['start'],sc[1]['end']))*100/sc[1]['max']-sc[1]['min'], sc[1],"body :",(abs(sc[1]['start']-sc[1]['end'])*100/sc[1]['max']-sc[1]['min']) ,"lower :", (min(sc[0]['start'],sc[0]['end'])-sc[0]['min'])*100/sc[0]['max']-sc[0]['min'])
    # print(sc[2], ":", "upper :" ,(sc[1]['max']-max(sc[2]['start'],sc[2]['end']))*100/sc[2]['max']-sc[2]['min'], sc[2],"body :",(abs(sc[2]['start']-sc[2]['end'])*100/sc[2]['max']-sc[2]['min']) ,"lower :", (min(sc[0]['start'],sc[0]['end'])-sc[0]['min'])*100/sc[0]['max']-sc[0]['min'])


    

# check()
