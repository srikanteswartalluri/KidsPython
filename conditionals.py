num = 11
condition1 = (num % 2 == 1)
print(condition1)
condition2 = (num % 5 == 0)
print(condition2)


if condition1 and condition2:
    print("number is odd and divisible by 5 ")
else:
    print("Not desired number")