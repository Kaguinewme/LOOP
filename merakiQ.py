#print even number between user
user=int(input("enter your number"))
i=1
while i<user:
    if i%2==0:
        print( i,end=" ")
    i=i+1