def register_user(database, name, email, age):
    if email in users_db:
        print(f"This email in base already {email}")
        return users_db
    if not "@" in email:
        print(f"This email in not right email {email}") 
        return users_db
    if age<18:
        print(f"Too yung {age}")
        return users_db
    users_db[email]= {"name": name, "age": age}
    print(f"Users {name} was registered")
    return users_db
users_db = {}
user_count= int(input("Введіть кількість студентів: "))

for i in range(user_count):
    print(f"Реєстрація {i+1} студента:")
    user_name = input("Введіть ваше ім'я: ")
    user_email = input("Введіть ваш email: ")
    user_age = int(input("Введіть ваш вік: "))
    users_db = register_user(users_db, user_name, user_email, user_age)


print(users_db)