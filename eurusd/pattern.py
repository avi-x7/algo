import time
import json
# def check():
#     with open('cndl.json', 'r+') as file:
#         data = json.load(file)
#     #print(data.keys())
#     #print(list(data.values())[0])
#     f1=list(data.values())[0]
#     f2=list(data.values())[1]
#     f3=list(data.values())[2]
    #start_matching
    #print(f1,f2['start'],f3['end'])

def is_hammer(_data,n):
    candle=list(_data.values())[n]
    max_price = float(candle['max'])
    min_price = float(candle['min'])
    start_price = float(candle['start'])
    end_price = float(candle['end'])
    price_diff = max_price - min_price

    # if price_diff >= 0.0002:
    #     if start_price < end_price and 11>((end_price - start_price) * 100 / price_diff) <= 45 and start_price >= (max_price + min_price) / 1.7:
    #         return True
    #     elif start_price < end_price and 11>((start_price - end_price) * 100 / price_diff) <= 45 and end_price <= (max_price + min_price) / 1.7:
    #         return True
    body_size = abs(start_price - end_price)
    lower_shadow_size = abs(min_price - min(start_price, end_price))
    upper_shadow_size = abs(max(start_price, end_price) - max_price)
    if ((upper_shadow_size)>(2*body_size)) or ((lower_shadow_size) > (2 * body_size)) :
      return True
    else:
      return False
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
      
def is_body(_data,n,b):
    candle=list(_data.values())[n]
    max_price = float(candle['max'])
    min_price = float(candle['min'])
    start_price = float(candle['start'])
    end_price = float(candle['end'])
    price_diff = max_price - min_price
    if ((abs(start_price-end_price)*100)/(price_diff) )<= b:
        return True

def is_morning_star(candle1, candle2, candle3):
   # Check if candle1 is a long red candle
   if float(candle1['start']) < float(candle1['end']):
       # Check if candle2 is a small or doji green candle
       if (abs(float(candle2['start']) - float(candle2['end']))) <((float(candle2['max']) - float(candle2['min'])) * 0.1):
           # Check if candle3 is a long green candle
           if float(candle3['start']) > float(candle3['end']):
               return True
   return False

def is_evening_star(candle1, candle2, candle3):
   # Check if the first candlestick is green
   if float(candle1['start']) > float(candle1['end']) :
       # Check if the second (candlestick is small
       if (abs(float(candle2['start']) - float(candle2['end']))) < ((float(candle2['max']) - float(candle2['min'])) * 0.1):
           # Check if the third (candlestick is red
           if float(candle3['start']) < float(candle3['end']):
               # Check if the closing price of the third (candlestick is below the middle of the first (candlestick
               if float(candle3['end']) < ((float(candle1['start']) + float(candle1['end'])) / 2):
                  return True
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
