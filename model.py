import os
import time
import model_helper as helper
import datetime

def add_item(item):
    try:
        item.replace(" ","")
        os.makedirs("watchlist/"+item)
    except OSError as e:
        print(e)

def add_link(item,link,type):
    item.replace(" ","")
    with open("watchlist/"+item+"/"+type,"w") as f:
        f.write(link)

def show_items():
    items=[]
    try:
        items=[x[0][10:] for x in os.walk("watchlist")][1:]
    except:
        pass
    return items

def checktypes(item):
    items = []
    try:
        items=[x[2] for x in os.walk("watchlist/"+item)][0]
        ite = []
        for item in items:
            if item == "Flipkart":
                ite.append("Flipkart")
            elif item == "Amazon":
                ite.append("Amazon")
    except OSError as e:
        pass
    return ite

def save_data(path,datum):
    path = path+"Data"
    with open(path,'a+') as f:
        x = str(datetime.date.today())
        y = str(datum)
        tupl = x+"\t"+y+"\n"
        f.write(tupl)

def probe():
    items = show_items()
    for item in items:
        types = checktypes(item)
        for type in types:
            path = "watchlist/"+item+"/"+type
            with open(path) as f:
                link = f.read()
            datum = helper.checkprice(link,type)
            save_data(path,datum)

probe()
