import os 
path='c:/Users/kuany/OneDrive/Рабочий стол/old'
print("Only folders:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
print('Only files:')
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
print("\nAll folders and files :")
print([ name for name in os.listdir(path)])
