import re
logs = [
    "2026-09-24 10:15:32 INFO User 123 logged in",
    "2026-09-24 10:16:04 ERROR User 456 authentication failed",
    "2026-09-24 10:17:21 INFO User 123 opened page",
    "2026-09-24 10:18:45 WARNING User 789 too many requests",
    "2026-09-24 10:19:02 ERROR User 123 database connection failed",
]
pattern = r"(?P<datetime>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>INFO|WARNING|ERROR) User (?P<user_id>\d+) (?P<message>.+)"
res = []
for s in logs:
    m = re.search(pattern, s)
    row = {
        "datetime": m.group("datetime"),
        "level": m.group("level"),
        "user_id": m.group("user_id"),
        "message": m.group("message"),
    }
    res.append(row)
for dict in res:
    for key in dict.keys():
        print(f"{key}:{dict[key]}")
    print("")