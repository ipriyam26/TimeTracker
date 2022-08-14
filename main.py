
from tinydb import TinyDB, Query
from sys import argv
import time as tt
import json
import termtables as t
from datetime import datetime

def show_table(db):
    data=[]
    headers = ["Subject", "Time"]
    for item in db:
        current_data = [item['name'],f"{'{:.2f}'.format(item['time']/3600)}H"]
        data.append(current_data)
    answere = t.to_string(data=data,header=headers,style=t.styles.ascii_thin_double)
    print(answere)
def show_full_table(db):
    data=[]
    headers = ["Subjects", "Time","Slots"]
    print(db.all())
    for item in db:
        # ck = '\n'.join(item['slots'])
        p='\n'.join([ str(itema).replace("{","").replace("}","").replace("'","") for itema in item['slots']])
        # print(p)
        current_data = [item['name'],f"{'{:.2f}'.format(item['time']/3600)}H",p]
        data.append(current_data)
    answere = t.to_string(data=data,header=headers,style=t.styles.ascii_thin_double)
    print(answere) 
    # print(current_data)   
        
    
def check_in(name:str):
    with open("temp.txt",'w') as f:
        f.write(f"{name.upper()}:{tt.time()}")

def check_out():
    name=""
    time = 0.0
    with open("temp.txt",'r+') as f:
        str = f.read()
        name = str.split(':')[0]
        time = float(str.split(':')[1])
    time_to_be_added = tt.time() - time
    find = Query()
    start = datetime.fromtimestamp(time).strftime("%I:%M, %B %d, %Y")
    end = datetime.fromtimestamp(tt.time()).strftime("%I:%M,  %B %d, %Y")

    if(db.contains(find.name == name)):
        db.update({'time': db.get(find.name == name)['time'] + time_to_be_added,'slots':db.get(find.name==name)['slots'].append({start:end})}, find.name == name)
    else:
        item = {"name":name, "time":time_to_be_added,'slots':[{start:end}]}
        db.insert(item)

db = TinyDB('db.json')
if(len(argv)>2):
    if(argv[1]=='check_in'):
        check_in(argv[2])
elif(len(argv)>1 ):
    if(argv[1]=='check_out'):
        check_out()
    elif(argv[1]=='show_full'):
        show_full_table(db)
        
else:
    show_table(db)
        


