def factorial(n):
    out=1
    while n>0:
        rem=n%10
        out=out+rem
        n=n//10
    return out
n=int(input("enter a number:"))
print(factorial(n))