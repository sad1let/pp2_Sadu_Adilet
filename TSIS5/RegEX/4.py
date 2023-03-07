import re

pattern = r'[A-Z][a-z]+'

test_string = str(input())

matches = re.findall(pattern, test_string)

print(matches)