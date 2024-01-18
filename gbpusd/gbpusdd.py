import requests
import time
import datetime
import pattern
import json
import c_ema
import c_sr
import threading
import concurrent.futures
## Old logics started
candles = {}
# if a=0 pass ,a=1 then buy ,a=2 sell
a=0 
# b is used of updatig sr
b=0
#c is used to run check patterns     
c=0

def check_pattern():
    # print(f'checking_patterns')
    with open('cndl.json', 'r') as fl:
        dat = json.load(fl)
        global a,c
        

        #downtrend to uptrend pattern +=> Buy
        def check_hammer_dozi():

        #hammer pattern
            if pattern.is_red(dat,2) and pattern.is_hammer(dat,1) and pattern.is_green(dat,0):
                print(f'hammer',end=" ")
                _x=0
                while _x<=400:
                    if float(list(dat.values())[0]['max']) < float(requests.get('http://localhost:3000/request/gbpusd').text):
                        requests.get('http://localhost:3000/gbpusd/'+"buy")
                        print("hammer found",end=" ")
                        c=0
                        break
                    else:
                        time.sleep(.5)
                        # print("else",float(list(dat.values())[0]['max']) , (requests.get('http://localhost:3000/request/gbpusd').text))
                        _x+=1
        def check_mo_star():
             if pattern.trend(dat) == "down":
                #  print(f'checking_morning_star' )
                 if pattern.is_morning_star(list(dat.values())[3],list(dat.values())[2],list(dat.values())[1],list(dat.values())[0]):
                    print("morning star",end=" ")
                    _x=0
                    while _x<=400:
                        if float(list(dat.values())[0]['max']) < float(requests.get('http://localhost:3000/request/gbpusd').text):
                            requests.get('http://localhost:3000/gbpusd/'+"buy")
                            print("morning star found",end=" ")
                            c=0
                            break
                        else:
                            time.sleep(.5)
                            _x+=1

        # uptrend to downtrend +==> sell
        def check_shoot_hang():
            if pattern.is_green(dat,3) and pattern.is_green(dat,2) and pattern.is_shooting_star(dat,1) and pattern.is_red(dat,0):
                print("shoot",end="")
                _y=0
                while _y<=400:
                    if float(list(dat.values())[0]['min']) > float(requests.get('http://localhost:3000/request/gbpusd').text):
                        requests.get('http://localhost:3000/gbpusd/'+"sell")
                        print("shooting star found",end=" ")
                        c=0
                        break
                    else:
                        time.sleep(.5)
                        _y+=1
            elif pattern.is_green(dat,3) and pattern.is_green(dat,2) and pattern.is_hanging_man(dat,1) and pattern.is_red(dat,0):
                print("hang",end="")
                _y=0
                while _y<=400:
                    if float(list(dat.values())[0]['min']) > float(requests.get('http://localhost:3000/request/gbpusd').text):
                        requests.get('http://localhost:3000/gbpusd/'+"sell")
                        print("hanging man found",end=" ")
                        c=0
                        break
                    else:
                        time.sleep(.5)
                        _y+=1


        def check_ev_star():
            if pattern.trend(dat) == "up":
                print(datetime.datetime.now().time())
                if pattern.is_evening_star(list(dat.values())[3],list(dat.values())[2],list(dat.values())[1],list(dat.values())[0]):
                    print(" evening star", end=" ")
                    _x=0
                    while _x<=400:
                        if float(list(dat.values())[0]['min']) > float(requests.get('http://localhost:3000/request/gbpusd').text):
                    # if float(list(dat.values())[0]['min']) < float(list(candles.values())[0]['min']):
                            requests.get('http://localhost:3000/gbpusd/'+"sell")
                            print("evening star found",end=" ")
                            c=0
                            break
                        else:
                            time.sleep(.5)
                            _x+=1
        with concurrent.futures.ThreadPoolExecutor() as executor:
                     executor.submit(check_hammer_dozi)
                     executor.submit(check_mo_star)
                     executor.submit(check_shoot_hang)
                     executor.submit(check_ev_star)
# t1 = threading.Thread(target=check_pattern)
def op():
    
    def c_cndl():
         
        g= requests.get('http://localhost:3000/request/gbpusd').text
        # print(g,datetime.datetime.now())
        _ch = datetime.datetime.now().hour
        _cm = datetime.datetime.now().minute
                             # print("candle is being created")
    # Round down the minute to the nearest multiple of 5
        _cm = (_cm // 5) * 5 
    # Get the current time
        c_tme = str(_ch) + ":" + str(_cm).zfill(2)
        # live=candles
        # print(c_tme,"fuckk",candles)
    # Check if the minute already exists in the dictionary
        if c_tme not in candles:
        # If the minute doesn't exist, initialize it with the current values
            candles[c_tme] = {
            # 'time': c_tme,
                'start': g,
                'max': g,
                'min': g,
                'end': g
                    }
        else:
        # If the minute already exists, update the values accordingly
            _c = candles[c_tme]
            _c['max'] = max(_c['max'], g)
            _c['min'] = min(_c['min'], g)
            _c['end'] = g

    def wtf(candles):
        if len(candles) >= 2:
                _sk, _sv = list(candles.items())[0]
                # print(_sk,"&",_sv)
                with open('cndl.json', 'r+') as file:
                        data = json.load(file)
                        # print(type(data))
                        data = {_sk: _sv, **data}
                        file.seek(0)
                        json.dump(data, file, indent=4)
                        file.truncate()
                        # print(candles)
                del candles[list(candles.keys())[0]]
                # c_ema.update_ema()
                with concurrent.futures.ThreadPoolExecutor() as executor:
                     executor.submit(check_pattern)
                # c_sr.upcrg()
                # t1.start()
                # global b
                # b=1
                global c
                c=1


    def alfcndl(candles):
        while True:
                c_cndl()
                wtf(candles)
                time.sleep(0.5)
        
    alfcndl(candles)

# def sr_update():
#         global b
#         while True:
#                 if b==1:
#                         time.sleep(200)
#                         #run update function
#                         b=0
#                 elif b==0:
#                         time.sleep(0.5)


# def check():
#         while True:
#                 global c
#                 if c==1:
#                         check_pattern()
#                         c==2
#                 elif c==2:
#                         time.sleep(240)
#                         c=0
#                 elif c==0:
#                         time.sleep(0.5)
op()



