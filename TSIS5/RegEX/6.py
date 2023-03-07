import re

pattern = r'[ ,.]'

test_string = 'Hello, world. How are you?'

new_string = re.sub(pattern, ':', test_string)

print(new_string)