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
    {"type": "out", "item": "Apple", "count": 15}, # Опа, а тут яблук не вистачить!
    {"type": "in", "item": "Mango", "count": 7}   ]
def get_stock_report(final_stock, actions):
    out_of_stock = []
    sales_count = {}
    new_stock = final_stock.copy()
    for i in actions:
        if i["type"]=="in":
            if i["item"] not in new_stock:
                new_stock[i["item"]]=i["count"]
            else:
                new_stock[i["item"]]+=i["count"]
        if i["type"]=="out":
            if i["item"] not in new_stock:
                continue
            if i["count"]> new_stock[i["item"]]:
                print ("Недостатньо товару:", i["item"])
            else:
                new_stock[i["item"]]-=i["count"] 
                current_item=i["item"]
                if current_item not in sales_count:
                    sales_count[current_item]=0
                    sales_count[current_item]+=1

    for k in new_stock:
        if new_stock[k]==0:
            out_of_stock.append(k)
            print (f'Out of stock: {k}')

    return(new_stock, sales_count, out_of_stock)
print(get_stock_report(stock, transactions))

