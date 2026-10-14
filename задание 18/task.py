import re
import json
import logging
logging.basicConfig(
    level=logging.INFO,
    filename="logs.txt",
    filemode="w",
)
errors_count = 0 
http_met = {}
url_dict = {}
with open("access.log", "r", encoding="utf-8") as f:
    for s in f:
        user_ip = re.search("\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}",s).group()
        user_http = re.search("[A-Z]{1,4}",s).group()
        user_url = re.search("[/][a-z]+\\.?/?[a-z]*",s).group()
        user_code = s[-4:-1:1]
        if user_http not in http_met.keys():
            http_met[user_http] = 1
            logging.info(f"Добавлен, новый HTTP {user_http}")
        else:
            http_met[user_http] += 1
            logging.info(f"По адресу {user_http} был сделан еще  1 запрос")
        if user_code[0] == "4":
            errors_count += 1
            logging.error(f"Ошибка {user_code}")
        if user_url not in url_dict.keys():
            url_dict[user_url] = 1
            logging.info(f"Добавлен новый URL {user_url}")
        else:
            url_dict[user_url] += 1
            logging.info(f"По URL был сделан еще 1 запрос.")
frequent_url = max(url_dict, key=url_dict.get)
result = {
    "Методы": http_met,
    "Наиболее частый URL": frequent_url,
    "Количество ошибок": errors_count
}
with open ("answer.json", "w", encoding="utf-8") as ans:
    
    json.dump(result, ans, ensure_ascii=False, indent=2)

