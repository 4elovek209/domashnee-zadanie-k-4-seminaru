import csv 
exp = open("expensive.csv")
with open("products.csv", mode="r", encoding="utf-8") as prod,\
    open("expensive.csv",mode="w",encoding="utf-8") as exp:
        reader = csv.DictReader(prod)
        writer = csv.DictWriter(exp, fieldnames = reader.fieldnames)
        writer.writeheader()
        for row in reader:
            name = row["name"]
            category = row["category"]
            price = int(row["price"])
            if price > 100:
                writer.writerow(row)
