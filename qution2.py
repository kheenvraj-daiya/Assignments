def factorial(y):
    result = 1
    for x in range(1, y + 1):
        result *= x
    return result
y=int(input("a positive integer:"))
print(factorial(y))
        

