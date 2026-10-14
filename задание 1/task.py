count_words =  0
count_symbols = 0
count_lines = 0
max_len = 0
with open("test.txt", "r", encoding='utf-8') as f:
    for line in f:
        count_words += 1
        for x in line:
            if x == ' ':
                count_words += 1
        count_symbols += len(line)
        count_lines += 1
        max_len = max(len(line),max_len)
print(count_lines, "Количество линий")
print(count_words, "Количество слов")
print(count_symbols,"Количество символов")
print(max_len, "Максимальная длина")
