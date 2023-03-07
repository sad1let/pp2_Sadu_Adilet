import re

pattern = r'a.*b$'

test_strings = ['acb', 'a1234b', 'a_b', 'ab', 'acbb']

for test_string in test_strings:
    match = re.search(pattern, test_string)
    if match:
        print(f"{test_string} matches the pattern")
    else:
        print(f"{test_string} does not match the pattern")