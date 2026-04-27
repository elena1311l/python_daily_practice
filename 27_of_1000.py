import math 

def math_test(number):
    koren = math.sqrt(number) 
    pi_val = math.pi          
    return koren, pi_val

print(math_test(16))

import random

def get_random_bonus(salary):
    num = random.randint(500, 2000) 
    print(num)
    sal=num+salary
    return sal
print(get_random_bonus(1000))

def pick_lucky_one(staff_list):
    res=random.choice(staff_list)
    return res
print(pick_lucky_one(["Anna", "Olena", "Max", "Kate"]))

def safe_bonus(salary, bonus):
    n_salary=0
    try:
        n_salary=salary+bonus
    except TypeError:
        print(f'it is not a number {bonus}')
    return n_salary
print('----salary-----')
print(safe_bonus(10000, 67))

def calculate_ratio(total, part):
    try:
        return total/part
    except TypeError:
        return (f'It is not a number {part}')
    except ZeroDivisionError:
        return (f'You can not do this with  {part}')
print(calculate_ratio(100, 20))
print(calculate_ratio(100, 0))
print(calculate_ratio(100, "two"))

def process_transaction(amount, balance):
    try:
        return balance-amount
    except TypeError:
        return (f'It is not a sum {amount}')
    finally:
        print('Transaction id end')
print('------ATM --------')
print(process_transaction(200, 1000))
print(process_transaction("two", 1000))
print(process_transaction(200, 1000))

