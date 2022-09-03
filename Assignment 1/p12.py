a=int(input("enter the number of a "))
b=int(input("enter the number of b "))
c=int(input("enter the number of c "))
if a>b:
    print(a,"is the greatest number")
elif a>c:
    print(a,"is the greatest number")
elif b>c:
    print(b,"is the greatest number")
elif c>b:
    print(c,"is the greatest number")
else:
    print("all numbers are same")