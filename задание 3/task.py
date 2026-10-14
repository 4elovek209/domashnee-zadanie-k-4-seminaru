import csv
total_score = 0
total_users = 0
max_score = -1
best_student = ''
groups_sl = {}
with open("users.csv", mode='r', encoding="utf-8") as users:
    reader = csv.DictReader(users)
    for row in reader:
        name = row['name']
        group = row['group']
        score = int(row['score'])
        #1
        total_score += score 
        total_users += 1
        #2
        if score > max_score:
            best_student = name
            max_score = score
        #3
        if group not in groups_sl:
            groups_sl[group] = []
        groups_sl[group].append(score)

print(f"Средний балл {total_score/total_users}")

print(f'Лучший студент {best_student}')
print("Средний балл групп")
for group,scores in  groups_sl.items():
    group_avg = sum(scores) / len(scores)
    print(group, group_avg)
