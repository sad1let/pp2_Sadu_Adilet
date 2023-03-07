def snake_to_camel(snake_str):
    words = snake_str.split('_')

    camel_words = [words[0]] + [word.capitalize() for word in words[1:]]

    camel_str = ''.join(camel_words)

    return camel_str


snake_str = 'hello_world_how_are_you'
camel_str = snake_to_camel(snake_str)
print(camel_str)