import re

for i in range(int(input())):
    
    if bool(re.match(r'^(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})(?:([0-9a-zA-Z])(?!.*\1)){10}', input())):
        print('Valid')
    else:
        print('Invalid')

