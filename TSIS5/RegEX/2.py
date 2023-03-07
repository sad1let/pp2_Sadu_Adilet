import re

pattern = r'a(b{2,3})'

test_strings = list(map(str,input().split()))

for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")