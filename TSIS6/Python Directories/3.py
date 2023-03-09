import os

path = input("Enter a path: ")

if os.path.exists(path):
    print("Path exists.")

    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print(f"Filename: {filename}")
    print(f"Directory: {directory}")

else:
    print("Path does not exist.")