from fastapi import FastAPI
app=FastAPI()

orders = [
    {"order_id": 1, "items": [{"name": "Pizza", "price": 200}, {"name": "Cola", "price": 50}], "status": "completed"},
    {"order_id": 2, "items": [{"name": "Burger", "price": 150}, {"name": "Fries", "price": 60}], "status": "pending"},
    {"order_id": 3, "items": [{"name": "Pizza", "price": 200}, {"name": "Coffee", "price": 80}], "status": "completed"}
]

@app.get("/revenue")
def get_total_revenue():
    all_sum=[]
    for i in orders:
        if i["status"]=="completed":
            for j in i["items"]:
                all_sum.append(j["price"])
    return int(sum(all_sum))

@app.get("/sales/{item_name}")
def count_item_sales(item_name):
    number=0
    for k in orders:
        if k["status"]=="completed":
            for l in k["items"]:
                if l["name"]==item_name:
                    number+=1
    return number

print(get_total_revenue())
print(count_item_sales( "Pizza"))

