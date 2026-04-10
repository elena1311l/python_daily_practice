
def add_task(database, task_name, priority):

    allowed = ["високий", "середній", "низький"]
    if priority not in allowed:
        print (f'Stranght format {priority}')
        return database
    else:
        database[task_name]=priority
        return database
    
def print_report(database):
    for key, values in database.items():
        print (f'To do: {key}, priority {values}')
    return database

def count_by_priority(database, priority_to_find):
    count=0
    for key, values in database.items():
        if values==priority_to_find:
            count+=1
    return count

tasks_db = {}
while True:
    task_name=input('To do:')
    if task_name == 'stop':
        break
    priority=input('Priority:')

    tasks_db = add_task(tasks_db, task_name, priority)
    print(tasks_db)
print (print_report(tasks_db))

high_count = count_by_priority(tasks_db, "високий")
medium_count = count_by_priority(tasks_db, "середній")
low_count = count_by_priority(tasks_db, "низький")
print(count_by_priority(tasks_db, "високий"))
print(count_by_priority(tasks_db, "середній"))
print(count_by_priority(tasks_db, "низький"))
print (f'Number of high priority tasks: {high_count}, medium {medium_count}, low {low_count}')
    



