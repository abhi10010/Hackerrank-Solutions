import re

regex = '^[a-zA-Z0-9_-]+[@][a-zA-Z0-9]+[.]+[a-zA-Z]{2,3}$'

def fun(s):
    if re.search(regex, s):
        return True
    else:
        return False
