import random

hero = {
    "name": "You",
    "hp": 100,
    "gold": 10
}
inventory = ["knif", "money", "battery"]

def buy_item(gold_on_hand, price, name):
    if gold_on_hand >=price:
        new_balance=gold_on_hand-price
        print(f'You boght {name} and price was {price}')
        return new_balance,  True
    return gold_on_hand, False

current_gold = hero["gold"]
new_balance, success = buy_item(current_gold, 11, "life")

hero["gold"]=new_balance
if success:
    inventory.append("life")

print(f"Hero stats: {hero}")
print(f"Inventory: {inventory}")




