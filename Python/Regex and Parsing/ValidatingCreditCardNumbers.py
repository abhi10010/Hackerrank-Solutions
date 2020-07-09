import re

pattern = re.compile(r"^(?!.*(\d)(-?\1){3})[4-6]\d{3}(-?\d{4}){3}$")

for _ in range(int(input())):
    print("Valid" if pattern.search(input()) else "Invalid")
