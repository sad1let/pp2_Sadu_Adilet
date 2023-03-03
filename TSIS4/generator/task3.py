def  func(n):
    return [i for i in range(0,n+1) if i %4==0 and i%3==0]
numbers=int(input())
print(func(numbers))