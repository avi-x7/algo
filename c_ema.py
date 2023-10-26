import json

def calculate_ema(data, period, previous_ema):
    alpha = 2 / (period + 1)
    end_value = float(data[0]['end'])
    current_ema = (end_value - previous_ema) * alpha + previous_ema
    return round(current_ema, 6)

def update_ema():
    with open('cndl.json', 'r+') as file:
        data = json.load(file)
        c_m = list(data.keys())
    # Load the previous EMA from the 'ema.json' file
    with open('ema.json', 'r+') as _ef:
        _d = json.load(_ef)
        try:
            previous_ema8 = float(_d["8"][c_m[1]])
            previous_ema20= float(_d["20"][c_m[1]])
            previous_ema50 = float(_d["50"][c_m[1]])
        except KeyError:
            previous_ema8 = float(list(data.values())[0]['end'])
            previous_ema20 = float(list(data.values())[0]['end'])
            previous_ema50 = float(list(data.values())[0]['end'])
            # print(_d["8"])
    # Calculate the new EMA for the latest data point
    e8 = calculate_ema(list(data.values()), 8, previous_ema8)
    e20 = calculate_ema(list(data.values()), 20, previous_ema20)
    e50 = calculate_ema(list(data.values()), 50, previous_ema50)
    # Update the 'ema.json' file with the new EMA
    # print("im working")
    with open('ema.json', 'r+') as _ef:
        # print("im too")
        _d = json.load(_ef)
        _d["8"][c_m[0]] = e8
        _d["20"][c_m[0]] = e20
        _d["50"][c_m[0]] = e50
        _ef.seek(0)
        json.dump(_d, _ef, indent = 4)
        print(c_m[0])

# update_ema()