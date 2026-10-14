import re
s = open("urls.txt").readline()
pattern = r"https://[^\s.?!,].[^\s,]*|http://[^\s.?!,].[^\s,]*"
for matches in re.finditer(pattern,s):
    print(matches.group())
