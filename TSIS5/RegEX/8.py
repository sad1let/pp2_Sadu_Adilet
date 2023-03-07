import re

pattern = r'[A-Z][^A-Z]*'

test_string = 'HelloWorldHowAreYou'

split_list = re.findall(pattern, test_string)

print(split_list)