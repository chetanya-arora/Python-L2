import re

with open("assets/some.txt", "r") as f:
    s = f.read()
    print(re.findall(r'\b\w[aeiouAEIOU]{2}\w\b', s))
