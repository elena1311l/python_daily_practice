from fastapi import FastAPI

app = FastAPI()

expenses = [
    {"category": "Food", "amount": 200, "date": "2026-04-01"},
    {"category": "Transport", "amount": 50, "date": "2026-04-01"},
    {"category": "Food", "amount": 150, "date": "2026-04-02"},
    {"category": "Entertainment", "amount": 300, "date": "2026-04-02"},
    {"category": "Transport", "amount": 20, "date": "2026-04-03"}
]

@app.get("/report")
def find_category():
    report = {}
    for i in expenses:
        if i["category"] not in report:
            report[i["category"]]=[i["amount"]]
        else:
            if i["category"] in report:
                report[i["category"]].append(i["amount"])
    for key, value in report.items():
        report[key] = sum(value)

    return report

@app.delete("/clear")
def clear_expenses():
    expenses.clear()
    return {"All data has been cleared"}

'''
print(find_category())
print(clear_expenses())
'''
