import os

path = input()

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print(f"File {path} has been deleted successfully.")
    else:
        print(f"File {path} cannot be deleted as it is not writable.")
else:
    print(f"File {path} does not exist.")
