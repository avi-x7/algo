import json
ss=[]
s=[]
sr=[]
r=[]

def upcrg():
    print("sr updated successfully")
    with open('cndl.json', 'r+') as _fl:
        _da = json.load(_fl)
        st=[]
        ed=[]
        for i, key in enumerate(_da):
            st.append(_da[key]['start'])
            ed.append(_da[key]['end'])
            if i == 6:  # We use 6 because enumeration starts at 0
                break
    cc="nnnnnnnn"
    for i in range(7):
        if (st[i] < ed[i]):
            cc = cc[:i] + 'g' + cc[i+1:]
        elif (st[i] > ed[i]):
            cc = cc[:i] + 'r' + cc[i+1:]
        else:
            cc = cc[:i] + 'n' + cc[i+1:]

    with open("sr.json","r+") as fsr:
        _da=json.load(fsr)
        if (cc[0]==cc[1]==cc[2]==cc[3]=='g' and cc[4]==cc[5]==cc[6]=='r'):
            _da["ss"].insert(0,st[3])
        elif (cc[0]==cc[1]==cc[2]=='g' and cc[3]==cc[4]==cc[5]==cc[6]=='r'):
            _da["ss"].insert(0,st[2])
        elif (cc[0]==cc[1]==cc[2]=='g' and cc[3]==cc[4]==cc[5]=='r'):
            _da["s"].insert(0,st[2])
        elif (cc[0]==cc[1]==cc[2]==cc[3]=='r' and cc[4]==cc[5]==cc[6]=='g'):
            _da["sr"].insert(0,st[3])
        elif (cc[0]==cc[1]==cc[2]=='r' and cc[3]==cc[4]==cc[5]==cc[6]=='g'):                  
            _da["sr"].insert(0,st[2])
        elif (cc[0]==cc[1]==cc[2]=='r' and cc[3]==cc[4]==cc[5]=='g'):
            _da["r"].insert(0,st[2])
    return cc



