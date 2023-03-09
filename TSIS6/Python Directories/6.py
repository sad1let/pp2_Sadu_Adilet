import string


for letter in range (64,91):
    filename = chr(letter) + ".txt"
    with open(filename, "w") as f:
        f.write(f"This is the text file for the letter {letter}")