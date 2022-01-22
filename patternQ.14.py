#1
#3 5
#7 9 11
#13 15 17 19
n=int(input("enter the rows"))
sum=1
i=1
while i<=n:
    j=1
    while j<=i:
        print(sum,end=" ")
        sum=sum+2
        j=j+1
    print()
    i=i+1
