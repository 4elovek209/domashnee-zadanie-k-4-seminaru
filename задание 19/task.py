import re
s = open("telephone_numbers.txt").readline()
print (re.findall("\\+7 \\d{3} \\d{3}-\\d{2}-\\d{2}|8 \\d{3} \\d{3}-\\d{2}-\\d{2}|\\+7 \\(\\d{3}\\) \\d{3}-\\d{2}-\\d{2}|8 \\(\\d{3}\\) \\d{3}-\\d{2}-\\d{2}",s))
