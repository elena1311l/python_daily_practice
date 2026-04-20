def word_frequency(text):
    lower_text=text.lower()
    new_text=lower_text.split()
    frequency = {}
    count=len(new_text)
    for item in new_text:
        if item not in frequency:
            frequency[item]=1
        else: 
            frequency[item]+=1
    return frequency, count
texts="Hello world I am here hello"
print (word_frequency(texts))

users = [
    {"name": "Alice", "role": "admin", "status": "active"},
    {"name": "Bob", "role": "user", "status": "banned"},
    {"name": "Charlie", "role": "user", "status": "active"},
    {"name": "Diana", "role": "admin", "status": "banned"}
]
def get_active_admins(user_list):
    admin=[]
    for item in user_list:
        if item["role"]=="admin" and item["status"]=="active":
            admin.append(item["name"])
    return admin
print (get_active_admins(users))

def promote_active_users(user_list):
    for item in user_list:
        if item["status"]=="active":
            item["role"]="super-user"
    return user_list
print ('new function')
print (promote_active_users(users))

people = [
    {"name": "Alice", "role": "admin", "achievements": ["first_login", "helper"]},
    {"name": "Bob", "role": "user", "achievements": ["first_login"]},
    {"name": "Charlie", "role": "user", "achievements": []}
]
def give_award(user_list, award_name):
    for it in user_list:
        it["achievements"].append(award_name)
    return user_list
print ('second new function')
print (give_award(people, "swimming"))

candidates = [
    {"name": "  ivan  ", "skills": "python, SQL, Excel", "years_exp": "2"},
    {"name": "OLGA", "skills": "HR, Recruitment", "years_exp": "5"},
    {"name": " petro", "skills": "Python, Java", "years_exp": "invalid"}
]

def clean_candidate_data(raw_data):
    for item in raw_data:
        item["name"]=item["name"].strip().capitalize()
        item["skills"]=item["skills"].lower().split(", ")
  
        if item["years_exp"].isdigit():
            item["years_exp"]=int(item["years_exp"])
        else:
            item["years_exp"]=0
    return raw_data
print('-----------------')


def find_it_recruiter(cleaned_data):
    selected_candidates = []
    for some in cleaned_data:
        if "python" in some["skills"] and some["years_exp"]>=2:
            selected_candidates.append(some["name"])
    return selected_candidates
print('last last last')

cleaned_list = clean_candidate_data(candidates)
it_stars = find_it_recruiter(cleaned_list)
print(f"Candidates for interview: {it_stars}")

def get_statistics(cleaned_list):
    total=len(cleaned_list)
    python_devs=0
    avg_exp=0
    print(f'Result total {total}')
    for item in cleaned_list:
        avg_exp+=item["years_exp"]
        if "python" in item["skills"]:
            python_devs+=1
    print(f'Result python_devs {python_devs}')
    print(f'Result avg_exp {avg_exp}')
    return avg_exp, python_devs, (avg_exp/total)

print (get_statistics(cleaned_list))
print(cleaned_list)



