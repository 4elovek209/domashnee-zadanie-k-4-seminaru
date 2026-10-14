from string import *
valid = (ascii_letters + digits + '-')
def is_valid_login(login):
    if login[0] in ascii_letters:
        if 4 <= len(login) <= 16:
            if all(x for x in login if x in valid):
                return True
    
    return False
print(is_valid_login(input()))
