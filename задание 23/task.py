import re
s = open("spaces.txt").readline()
s_clone = s
pattern = r"\s{2,}"
for match in re.finditer(pattern,s):
    bad = match.group()
    s = s.replace(bad," ")
    s = s.replace(bad," ")
print(s)
