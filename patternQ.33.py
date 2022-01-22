#1
#B B
#3 3 3
#D D D D
#5 5 5 5 5

n=5
i=1
while i<=n:
    j=1
    while j<=i:
        if i%2==0:
            print(chr(64+i),end=" ")
        else:
            print(i,end=" ")
        j+=1
    i+=1
    print()