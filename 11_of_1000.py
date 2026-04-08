# Початковий стан складу
stock = {
    "Apple": 10,
    "Banana": 5,
    "Orange": 0
}

# Список операцій: тип ("in" - приїхало, "out" - купили), назва товару та кількість
transactions = [
    {"type": "in", "item": "Apple", "count": 5},
    {"item": "Banana", "count": 2, "type": "out"},
    {"type": "in", "item": "Orange", "count": 10},
    {"type": "out", "item": "Apple", "count": 20}, # Опа, а тут яблук не вистачить!
    {"type": "in", "item": "Mango", "count": 7}    # Новий товар, якого не було в stock
]

new_stock=stock.copy()
def process_transactions(new_stock, actions):

    for i in actions:
        if i["type"]=="in":
            if i["item"] not in new_stock:
                new_stock[i["item"]]=i["count"]
            else:
                new_stock[i["item"]]+=i["count"]

        elif i["type"]=="out":
            if i["item"] not in new_stock:
                print ("Товару немає на складі:", i["item"])
                continue

            if i["count"] > new_stock[i["item"]]:
                new_stock[i["item"]]=new_stock[i["item"]]
                print ("Недостатньо товару:", i["item"])
            else:   
                new_stock[i["item"]]-=i["count"] 
    return new_stock

print (process_transactions(stock, transactions))