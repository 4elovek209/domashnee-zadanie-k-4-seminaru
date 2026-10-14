min_num = float('inf')
max_num = float('-inf')
sum_num = 0
count_num = 0
with open("big_numbers.txt",mode="r",encoding="utf-8") as f:
    for s in f:
        tk_num = int(s)
        count_num += 1
        min_num = min(min_num, tk_num)
        max_num = max(max_num,tk_num)
        sum_num += tk_num
print(sum_num)
print(min_num)
print(max_num)
print(count_num)
print(sum_num / count_num)
