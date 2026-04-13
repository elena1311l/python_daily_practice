import random

hero = {
    "name": "You",
    "hp": 100,
    "gold": 10
}
inventory = ["knif", "money", "battery"]

def choice_random():
    while True:
        i = input("Start program - random event or stop: ")
        if i== "stop":
            break
        ch=random.randint(1,3)
        print(ch)
        if ch==1:
            hero["hp"]-=10
            print(f'New hp {hero["hp"]}')
        elif ch==2:
            hero["gold"]+=5
            print(f'New gold {hero["gold"]}')
        else: 
            if ch==3:
                goods=input("Input new good:")
                inventory.append(goods)
                print(f'New inventory {inventory}')
    return(hero, inventory)
print(choice_random())

