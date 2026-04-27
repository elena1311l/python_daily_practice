def check_age(age):
    if age<0:
        raise ValueError ('It is imposible to be yanger 0 year')
    if age>150:
        raise ValueError ('It is impossible')
    return age   
try:
    print(check_age(152))
except ValueError:
    print ('Again not real age, too nig number')

try:
    print(check_age(-5))
except ValueError:
    print ('Again not real age')
print(check_age(19))


user_data = {"name": "Olena", "city": "Kyiv", "email": "a@gmail.com"}

def email_users(user_list):
    try:
        print(user_data["email"])
    except KeyError:
        print("Any Emai")

    email = user_data.get("email", "no-email")
    print(email)
print(email_users(user_data))


# file for reading 
with open("new_test.txt", "w") as file:
    file.write("Hello, Python world!")

print("Файл створено успішно!")


with open("new_test.txt", "a") as fl:
    fl.write("\nThis is a second line \n")

with open("new_test.txt", "a") as fl:
    fl.write("Anna, Alex, Ihor\n")

with open ("new_test.txt", "r") as f:
    r=f.read()
print(r)

with open("new_test.txt", "r") as f:
    lines = f.readlines()
    print(lines)

with open("new_test.txt", "r") as f:
    for line in f: 
        for word in line.split():
            if word.startswith("A"):
                print(f'we found {word}')

try:
    with open("new_low.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print(f'Sorry we could not find file {f}')
    pass

with open("new_test.txt", "r") as fl:
    text=fl.read()
    clean_text = text.replace(" ", "").replace("\n", "").replace("\r", "")
    lenn = len(clean_text)
    print(f'File havs {lenn} symbols')