import re

def user_regex(user):
    user_re = "^[A-z][A-z0-9-_]{3,23}$"
    pwd_re = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$"
    pwd_regex = re.findall(pwd_re, user.password)
    user_regex = re.findall(user_re, user.username)
    
    if pwd_regex and user_regex:
        return True
    else:
        return False


# class User():
#     usr = "Alface"
#     pwd = "!test123"

# user = User()

# user_regex(user)