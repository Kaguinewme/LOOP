
num=int(input("enter the number"))
i=1
count=0
while i<=num:
    if num%i==0:
        count= count+1
    i=i+1
if count==2:
    print("prime no")
    i=0
    rev=0
    while num>0:
        rev=rev*10+num%10
        num=num//10
    i=1
    count=0
    while i<=rev:
        if rev%i==0:
            count=count+1
        i=i+1
    if count==2:
        print("twisted prime no")
else:
    print("not")    
