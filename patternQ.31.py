#5 * 5 * 5
#4 * 4 *
#3 * 3
#2 *
#1

i=5
while i>=1:
    j=1
    while j<=i:
        if j%2==0:
           print("*",end=" ")
        else:
            print(i,end=" ")
        j+=1
    i-=1
    print()