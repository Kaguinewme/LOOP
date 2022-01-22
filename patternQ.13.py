
#1
#2 3
#4 5 6
#7 8 9 10
n=int(input("enter the rows"))
sum=1
i=1
while i<=n:
    j=1
    while j<=i:
        print(sum,end=" ")
        sum=sum+1
        j=j+1
    print()
    i=i+1

# for loop   
n=int(input("enter the rows"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
