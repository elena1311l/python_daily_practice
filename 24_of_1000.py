salaries = ["2000", "1500", "от 500", "3000", "N/A", "1200"]
def safe_convert(salary_list):
    clean_salaries=[]
    for item in salary_list:
        try:
            clean_salaries.append(int(item)*40)
        except ValueError:
            print (f'Помилка в даних{item}')
    
    return clean_salaries
print (safe_convert(salaries))

def calculate_average_salary(salaries_list):
    only_numbers = [item for item in salaries_list if isinstance(item, (int, float))]
    try:
        result=sum(only_numbers)/len(only_numbers)
        return result
    except ZeroDivisionError:
        return 0
sal = [1000, "skip", 2000, 3000]
print(calculate_average_salary(sal))
print(calculate_average_salary([]))

prices = {"apple": 20, "banana": 30, "orange": 25}
order = ["apple", "mango", "banana"]

def get_total_cost(price_dict, order_list):
    total_price=0
    for item in order_list:
        try:
            total_price+=price_dict[item]
        except KeyError:
            print(f'No goods {item} ')
    return total_price
print(get_total_cost(prices, order))

stock = [
    {"name": "Laptop", "price": 1000, "count": 2},
    {"name": "Mouse", "price": "25", "count": 10},  # Ціна — рядок!
    {"name": "Keyboard", "count": 5},               # Ціни взагалі немає!
    {"name": "Monitor", "price": 200, "count": "3"}, # Кількість — рядок!
    {} # Взагалі пустий словник!
]
def calculate_stock_value(items):
    total_sum = 0
    for item in items:
        try:
            total_sum+=int(item["price"])*int(item["count"])
            print(f'For {item} is {total_sum}')
        except KeyError:
            continue
        except ValueError:
            continue
        except TypeError:
            continue
    return total_sum
print('- - - - - - - TOTAL SUM - - - - - -')
print(calculate_stock_value(stock))

candidates = [
    {"name": "Anna", "skills": "Python, SQL", "exp": 3},
    {"name": "Ihor", "skills": "Java, C++", "exp": 5},
    {"name": "Olena", "skills": "Python, Git, Docker", "exp": "2"}, # Досвід — рядок!
    {"name": "Max", "skills": "Python", "exp": 1},
    {"name": "Daria", "exp": 4} # Навички взагалі не вказані!
]
def filter_candidates(candidate_list, required_skill, min_exp):
    name=[]
    for item in candidate_list:
        try:
            if required_skill in item["skills"].lower() and int(item["exp"])>=min_exp:
                name.append(item["name"])
            else:
                print(f'Any match for {item["name"]}')
        except KeyError:
            print(f'Any result for {item["name"]} ')
    return name
print('------------------------------------------')
print(filter_candidates(candidates, "python", 2))





        


