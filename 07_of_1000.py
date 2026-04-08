
from fastapi import FastAPI

app = FastAPI()

# Наша "база даних" матчів
matches = [
    {"player": "Olena", "score": 100, "result": "win"},
    {"player": "Ivan", "score": 50, "result": "loss"},
    {"player": "Olena", "score": 150, "result": "win"},
    {"player": "Andrii", "score": 200, "result": "win"},
    {"player": "Ivan", "score": 30, "result": "win"},
    {"player": "Andrii", "score": 100, "result": "loss"}
]

@app.get("/")
def home():
    return {"message": "Вітаємо у системі рейтингів!"}

@app.get("/leaderboard")
def show_leaderboard():
    result = {}
    for i in matches:
        if i["result"] == "win":
            p = i["player"]
            s = i["score"]
            if p in result:
                result[p] += s
            else:
                result[p] = s
    return result
print(show_leaderboard())

