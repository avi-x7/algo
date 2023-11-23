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
    if ((upper_shadow_size)>(2*body_size)) or ((lower_shadow_size) >  (2 *body_size)) :
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

def is_morning_star(candle1, candle2, candle3):
   # Check if candle1 is a long red candle
   if float(candle1['start']) > float(candle1['end']):
       # Check if float(candle2 is a small or doji green float(candle
       if (abs(float(candle2['start']) - float(candle2['end']))) <((float(candle2['max']) - float(candle2['min'])) * 0.1):
           # Check if float(candle3 is a long green float(candle
           if float(candle3['start']) < float(candle3['end']):
               return True
   return False

def is_evening_star(candle1, candle2, candle3):
   # Check if the first candlestick is green
   if float(candle1['start']) < float(candle1['end']) :
       # Check if the second float(candlestick is small
       if (abs(float(candle2['start']) - float(candle2['end']))) < ((float(candle2['max']) - float(candle2['min'])) * 0.1):
           # Check if the third float(candlestick is red
           if float(candle3['start']) > float(candle3['end']):
               # Check if the closing price of the third float(candlestick is below the middle of the first float(candlestick
               if float(candle3['end']) < ((float(candle1['start']) + float(candle1['end'])) / 2):
                  return True
   return False





    

# check()
