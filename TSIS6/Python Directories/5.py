filename = input("Enter the file name: ")
my_list = ['apple', 'banana', 'cherry']

try:
    with open(filename, 'w') as file:
        for item in my_list:
            file.write(item + '\n')
    print("List written to file successfully!")
except:
    print("Error writing to file.")