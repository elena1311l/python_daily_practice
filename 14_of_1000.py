prices = {
    "хліб": 20,
    "молоко": 35,
    "яблука": 50,
    "сир": 120
}

def calculate_total(cart):
    sum=0
    for i in cart:
        if i in prices:
            sum+=int(prices[i])
            print (prices[i])
        else:
            print(f'Sorry {i} not in prices ')
    return sum

tovar=[]
while True:
    i = input("Введіть ваше товар або стоп: ")
    if i== "стоп":
        break
    tovar.append(i)
        
print (calculate_total(tovar))

