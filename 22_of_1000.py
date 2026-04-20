job_requirements = ["python", "sql", "git"]

candidates = [
    {"name": "Ivan", "skills": ["python", "sql", "excel"], "years_exp": 2},
    {"name": "Olga", "skills": ["hr", "recruitment"], "years_exp": 5},
    {"name": "Petro", "skills": ["python", "git", "java"], "years_exp": 1}
]
def analyze_matching(candidate_list, requirements):
    for item in candidate_list:
        matches=0
        percent=0
        for rec in requirements:
            if rec in item["skills"]:
                matches+=1
        percent=(matches/ len(requirements)) * 100
        item["percent"]=percent
    return candidate_list
result=analyze_matching(candidates,job_requirements)
for j in result:
    print(f"{j['name']}: {j['percent']}%")
print(result)

def get_perfect_candidates(analyzed_list):
    shortlist=[]
    for item in analyzed_list:
        if item["percent"]>=50 and item["years_exp"]>=2:
            shortlist.append(item)
    return shortlist
print('result result result')
print(get_perfect_candidates(result))

