import json
new_data = []
with open("students.json", mode="r+", encoding="utf-8") as f:
    data = json.load(f)
    for row in data:
        name =  row["name"]
        age = row["age"]
        score =  int(row["score"])
        row["passed"] = False
        if score >= 60:
            row["passed"] = True
        new_data.append(row)
with open("new_students.json", mode="w", encoding="utf-8") as new_f:
    json.dump(new_data, new_f, ensure_ascii=False,indent=" ")
