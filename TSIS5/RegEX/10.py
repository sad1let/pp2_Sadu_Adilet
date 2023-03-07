def camel_to_snake(s):
    result = ''
    for c in s:
        if c.isupper():
            result += '_' + c.lower()
        else:
            result += c
    return result

s = 'HelloWorldHowAreYou'
new_s = camel_to_snake(s)
print(new_s)