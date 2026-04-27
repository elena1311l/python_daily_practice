products = {"Laptop": 1200, "Mouse": 25, "Keyboard": 150, "Monitor": 600, "USB-Hub": 40}

def get_expensive_items(products_dict):
    result=[]
    for key, value in products_dict.items():
        if value>=500:
            result.append(key)
    res=[key for key, value in products_dict.items() if value >=500]
    return result, res
print(get_expensive_items(products))

prices = [10, 15, 20, 25, 30]
def parna_f(prices_list):
    even_prices = []
    for item in prices_list:
        if item%2==0:
            even_prices.append(item)
    parn_price=[item for item in prices_list if item%2==0]
    
    return even_prices, parn_price
print(parna_f(prices))

names = ["anna", "olena", "ihor", "max"]
def uppercase_names(names_list):
    result=[]
    for item in names_list:
        result.append(item.upper())

    res=[item.upper() for item in names_list ]
    return result, res
print (uppercase_names(names))

salaries = [1000, 2000, 3000]
def give_bonus(salaries_list):
    new_sal=[]
    for item in salaries_list:
        n_item=item*1.1
        new_sal.append(n_item)

    n_sal=[item*1.1 for item in salaries_list]
    return new_sal, n_sal
print(give_bonus(salaries))
        
salaries = [1000, 2000, 3000, 1200, 5000]
def calculate_top_bonuses(sal_list):
    res=[]
    for item in sal_list:
        if item>1500:
            res.append(item*1.1)
        else:
            continue
    result=[item*1.1 for item in sal_list if item>1500]
    return res, result
print('-------------------------------')
print(calculate_top_bonuses(salaries))

salaries = [1000, 2000, 3000]

def complex_bonuses(sal_list):
    fin_sal=[]
    for item in sal_list:
        if item>1500:
            fin_sal.append(item*1.1)
        else:
            fin_sal.append(item*1.05)
    fin_salaries=[item*1.1 if item>1500 else item*1.05 for item in sal_list ]
    
    return fin_sal, fin_salaries
print('-------------------------------')
print(complex_bonuses(salaries))

def apply_custom_bonus(salari, percent=1.1):
    bonus=[]
    for item in salari:
            bonus.append(item*percent)

    list_bonus=[item*percent for item in salari]
    return bonus, list_bonus
print('--------------SALARIES----------------')
print(apply_custom_bonus(salaries, 2))

def show_skills(name, *skills):
    skill=[]
    skill=", ".join(skills)
    return (f'{name} have some skills {skill}')
print(show_skills("Olena", "Phyton", "Linux", "Java"))
    
def show_skills_pro(name, *skills):
    skill=[]
    new_item=[]
    for item in skills:
        new_item.append(item.capitalize())
    skill=", ".join(new_item) 

    n_item=[i.capitalize() for i in skills]

    return (f'This {name} have next skills {skill}'), (f'This {name} have next skills {n_item}')
print ('- - - good skills - - -')
print (show_skills_pro("Olena", "sql", "python", "linux"))

names = ["Anna", "Olexandr", "Max"]
def create_name(list_name):
    list={}
    for item in list_name:
        list[item]=len(item)

    res_list={item:len(item) for item in list_name}
    return list, res_list
print(create_name(names))

results = {"Anna": 85, "Max": 60, "Olexandr": 92, "Ihor": 70}
def result_test(list_result):
    res={}
    for key, value in list_result.items():
        if value>=75:
            res[key]=value

    new_res={k:v for k,v in list_result.items() if v>=75}
    return res, new_res

print('----result test-----')
print(result_test(results))

def build_profile(first, last, **user_info):
    profile = {
        'first_name': first,
        'last_name': last,}
    for key, value in user_info.items():
        profile[key]=value

    prof={key:value for key, value in user_info.items() }
    return profile, prof
my_user = build_profile("Olena", "B.", location="Ukraine", field="IT")
print(my_user)

def order_pizza(size, *toppings, **details):
    order={
        'size': size,
        'toppings': list(toppings),
        'details': details
    }

    for k, v in details.items():
        order[k]=v
    return order
print('--------order-------')
print(order_pizza("XL","chicken", "corn", "chezz", time="14-00", vul="vul Shevchenko" ))

def create_email(recipient, *tags, **content):
    email={
        'recipient': recipient,
        'tags': list(tags),
        'content': content
    }
    return email
print('-----email-------')
print(create_email("Hello", "python", "sql", text="Some text", end="some end"))

tax_rate = 0.2  # Податок 20%

def change_tax():
    tax_rate = 0.1  # Хочемо змінити на 10%
    return tax_rate

change_tax()
print(tax_rate) 

app_status = "Stop"




