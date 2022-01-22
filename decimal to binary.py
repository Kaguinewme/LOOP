print("enter the binary number:")
a=int(input("enter the number"))
d=0
rem=0
i=1
while a!=0:
    rem=a%10
    d=d+(rem*i)
    i=i*2
    a=int(a/10)
print(d)