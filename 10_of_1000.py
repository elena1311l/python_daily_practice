from fastapi import FastAPI
app=FastAPI()

inventory = [
    {"item": "Laptop", "price": 1000, "count": 5},
    {"item": "Mouse", "price": 20, "count": 10},
    {"item": "Keyboard", "price": 50, "count": 0}
]
@app.get("/available")
def get_available_items():
    result=[]
    for i in inventory:
        if i["count"]>0:
            result.append(i["item"])
    return {"available_items": result}

@app.get("/price/{item_name}")
def get_item_price(item_name):
    res=0
    for j in inventory:
        if j["item"]==item_name:
            res=j["price"]
    if res == 0:
        return {"error": "Товар не знайдено"}
        
    return {"item": item_name, "price": res}

print (get_available_items())
print (get_item_price( "Mouse"))
