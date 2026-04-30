import random
import json

reel1 = ["Seven"] * 1 + ["Cherry"] * 3 + ["Lemon"] * 6
reel2 = ["Seven"] * 1 + ["Cherry"] * 2 + ["Lemon"] * 7
reel3 = ["Seven"] * 1 + ["Cherry"] * 1 + ["Lemon"] * 8

with open('config.json', 'r') as setting:
    data = json.load(setting)

def simulate_slots(spins,data):
    res_sum = 0
    
    for _ in range(spins):
        result1=random.choice(reel1)
        result2=random.choice(reel2)
        result3=random.choice(reel3)
        if result1==result2==result3=="Seven":
            res_sum+=data["seven_win"]
        elif result1==result2==result3=="Cherry":
            res_sum+=data["cherry_win"]
        elif result1==result2==result3=="Lemon":
            res_sum+=data["lemon_win"]
        else:
            res_sum+=0
    return res_sum/ spins
temp=simulate_slots(100000, data)
results={
    "RTP": temp,
    "spins": 100000,
    "status": "Success",
    "current": "USD"
}
json_data=json.dumps(results, indent=4)
print(f"Result JSON")
print(json_data)

with open ('slot_report.json', "w") as f:
    json.dump(results, f, indent=4)