import re
product = [
    "PRD-12345",
    "PRD-00123",
    "USR-12345",
    "PRD-987",
    "PRD-ABCDE",
    "PRD-54321"
]
res = []
pattern = r"PRD-\d{5}"
for s in product:
    if re.search(pattern, s):
        res.append(s)
print(res)