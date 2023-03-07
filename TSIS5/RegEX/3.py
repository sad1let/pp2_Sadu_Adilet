import re

pattern = r'[a-z]+_[a-z]+'

txt = str(input())

matches = re.findall(pattern, txt)

print(matches)