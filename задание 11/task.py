import re 
users_id = []
users_id_with_error = []
with open ("logs.txt", mode="r", encoding="utf-8") as log:
    for s in log:
        id_user = re.search("\d+",s).group()
        if id_user not in users_id:
            users_id.append(id_user)
        is_ERROR = re.search("ERROR",s)
        if is_ERROR:
            print(s)
            if id_user not in users_id_with_error:
                users_id_with_error.append(id_user)
print("Все ID пользователей: ", *users_id)
print("ID пользователей, для которых вышла ошибка. ", *users_id_with_error)
