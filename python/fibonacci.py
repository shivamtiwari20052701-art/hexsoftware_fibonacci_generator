no=int(input("enter the number till you want in the series:"))
a=0
b=1
c=0
print(a)
print(b)
i=1
while i<no:
    c=a+b
    a=b
    b=c
    i=i+1
    print(c)