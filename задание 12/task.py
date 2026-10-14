import re
from string import *
emails_list = []
alp = ascii_lowercase
with open ("emails.txt", mode="r", encoding="utf-8") as em:
    for s in em:
        is_email = re.search(f"@+\\w.[{alp}]",s)
        if is_email and s not in emails_list:
            emails_list.append(s)
for em in emails_list:
    print(em)
