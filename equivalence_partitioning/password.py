import re

def check_password(passwd):
    valid_password = len(passwd) >= 8

    valid_password = valid_password and bool(re.findall(r'\d+',passwd))
    valid_password = valid_password and bool(re.findall(r'[A-Z]+',passwd))
    valid_password = valid_password and bool(re.findall(r'[a-z]+',passwd))

    return valid_password
