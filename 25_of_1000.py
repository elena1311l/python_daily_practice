skills_data = [
    "Python, SQL, Git",
    "Java, SQL, Docker",
    "Python, Docker",
    "Python, SQL, HTML",
    "Git, SQL"
]
def count_skills(data):
    skills_count = {}
    for item in data:
        skill=item.split(',')
        for i in skill:
            if i not in skills_count:
                skills_count[i]=1
            else:
                skills_count[i]+=1
    return skills_count
print(count_skills(skills_data)) 

team = {
    "Anna": ["Python", "SQL", "Git"],
    "Ihor": ["Java", "SQL"],
    "Olena": ["Python", "Docker"],
    "Max": ["Python"]
}
def find_specialists(team_dict, target_skill):
    people=[]
    for key, value in team_dict.items():
        if target_skill in value:
            people.append(key)
    return people
print('--------------------')
print(find_specialists(team, "Python"))


projects = [
    {"title": "E-commerce Site", "tech": ["Python", "Django", "PostgreSQL"]},
    {"title": "Mobile App", "tech": ["React Native", "Firebase"]},
    {"title": "Data Scraper", "tech": ["Python", "BeautifulSoup"]},
    {"title": "Chat Bot", "tech": ["Python", "Telegram API"]}
]
def analyze_projects(project_list, target_tech):
    found_titles=[]
    for item in project_list:
        if target_tech in item["tech"]:
            found_titles.append(item["title"])
    return found_titles, len(found_titles)
print('----------new  new  new ----------')
print(analyze_projects(projects, "Python")) 

sales_data = [
    {"product": "iPhone", "price": 1000, "quantity": 2},
    {"product": "MacBook", "price": 2500, "quantity": 1},
    {"product": "Case", "price": "20", "quantity": 5}, # Ціна — рядок
    {"product": "AirPods", "price": 200},             # Немає кількості!
    {}                                                # Порожній чек
]
def generate_report(sales):
    total_revenue = 0
    items_sold = 0
    for item in sales:
        try:
            total_revenue+=int(item["price"])*item["quantity"]
            items_sold+=item["quantity"]
        except KeyError: 
            print(f'Some empty {item}')
    return {"revenue": total_revenue, "total_items": items_sold}

print(generate_report(sales_data))


