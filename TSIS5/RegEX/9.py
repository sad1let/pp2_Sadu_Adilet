def insert_spaces(s):
    result = ''
    for i, c in enumerate(s):
        if c.isupper() and (i > 0 and s[i-1].islower() or i > 1 and s[i-2:i].isspace()):
            result += ' '
        result += c
    return result

s = 'HelloWorldHowAreYou'
new_s = insert_spaces(s)
print(new_s)