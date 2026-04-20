import random
inventory = ["apple", "gold", "axe", "stick", "nut"]

def advanced_filter(items_list, min_length):
    new_list=[]
    for item in items_list:
        if len(item)>=min_length or item=="gold":
            new_list.append(item)
        else:
            pass
    return new_list

filtered_inventory = advanced_filter(inventory, 4)
print(filtered_inventory)


hero = {"name": "Geralt", "hp": 80, "gold": 150}
inventorys = ["sword", "gold", "potion"]

def show_stats(hero_data, items_list):
    count=0
    for item in items_list:
        if item=="gold":
            count+=1
            
    print(f'This hero {hero_data["name"]} have a health {hero_data["hp"]}')
    if count>=1:
        print(f'Wow you have a {hero_data["gold"]} gold ')
    print(f'He has {len(items_list)} goods')

show_stats(hero, inventorys)

hero = {"name": "Geralt", "hp": 80, "gold": 150}
inventorys = ["sword", "gold", "potion"]
def random_event(man, event):
    if random.randint(1, 2)==1:
        print('We have resul 1')
        man["hp"]-=20
    else:
        event.append("silver")
        print('We have resul 2')
    return (man, event)

def show_stats(man, event):
    print("\n----------------------")
    if "silver" in event:
        print('Wow you have a silver!')
    print(f'Our {man["name"]} have some power {man["hp"]} and gold {man["gold"]}')
    for item in event:
        print(f'Godds is {item} ')
    print("------------------------\n")


print (random_event(hero,inventorys))
print(show_stats(hero,inventorys))
