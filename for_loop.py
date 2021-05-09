n = input("Enter a number")
n = int(n)
for i in range( n+1):
    #divisibility by 5
    if i % 5 == 0 and i % 3 == 0:
        print("Hello World")
    elif i % 5 == 0:
        print("Hello ")
    elif i % 3 == 0:
        print("World")
    else:
        print(i)
