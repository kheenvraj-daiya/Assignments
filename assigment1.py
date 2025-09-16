#question 1


def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    return x
x=int(input("larger number:"))
y=int(input("smaller number:"))
print(gcd(x,y))


    
    