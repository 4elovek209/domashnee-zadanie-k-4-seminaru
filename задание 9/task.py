import re
class ValueError():
    def __init__(self):
        pass
def parse_number(value):
    if re.fullmatch("-?\\d+\\.?\\d", value):
        return float(value)
    else:
        raise ValueError("Проверьте что вы ввели число")

print(parse_number(input()))
