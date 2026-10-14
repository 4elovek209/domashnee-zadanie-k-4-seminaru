import re
s = open("dates.txt").readline()
months31 =  ["01","03","05","07","08","10","12"]
months30 = ["04","06","09","11"]
month2829 = ["02"]
pattern = r"\b(0[1-9]|[12]\d|3[01])\.(0[1-9]|1[0-2])\.\d{4}\b"
def vis_year(n):
    if (n % 4 == 0 and n % 100 != 0) or n%400 == 0:
        return 1
    return 0
for match in re.finditer(pattern, s):
    found_data = match.group()
    dd = found_data[:2]
    mm = found_data[3:5:]
    yyyy = found_data[6:]
    if vis_year(int(yyyy)):
        if int(dd) <= 29:
            print(found_data)
        elif int(dd) == 30 and mm not in month2829:
            print(found_data)
        elif int(dd) == 31 and mm in months31:
            print(found_data)
    else:
        if int(dd) <= 28:
            print(found_data)
        elif 29<=int(dd)<=30 and mm not in month2829:
            print(found_data)
        elif int(dd) == 31 and mm in months31:
            print(found_data)
 