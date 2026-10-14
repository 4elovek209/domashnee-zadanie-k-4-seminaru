num = open("numbers.txt")
a = []
for s in num:
    try:
        a.append(int(s))
    except:
        print("В файле содержатся строки, которые, содержат другие символы.")
with open("result.txt","w", encoding="utf-8") as f:
    f.write(f"Максимальное значение {max(a)}\n")
    f.write(f"Минимальное значение {min(a)}\n")
    f.write(f"Среднее значение {(sum(a)/len(a))}")
