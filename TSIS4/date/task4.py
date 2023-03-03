from datetime import datetime

date1 = input("DD-MM-YY H:-M:-S:")
date2 = input("DD-MM-YY H:-M:-S:")

x = datetime.strptime(date1,'%d-%m-%Y %H:%M:%S')
y = datetime.strptime(date2,'%d-%m-%Y %H:%M:%S')

difference = (x-y).total_seconds()

print(difference)