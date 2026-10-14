count_errors = 0
count_warnings = 0
count_infos = 0
users_with_errors = []
with open("logs16.txt", mode="r", encoding="utf-8") as f:
    for s in f:
        if "ERROR" in s:
            count_errors += 1
        if "INFO" in s :
            count_infos += 1 
        if "WARNING" in s:
            count_warnings += 1
print(f"ERRORS: {count_errors}")
print(f"INFOS: {count_infos}")
print(f"WARNINGS: {count_warnings}")
