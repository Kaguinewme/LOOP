#print 1 to 100 and even no should print with negative sign 
n=100
i=1
while i<=n:
    if i%2==0:
        print( ",",i*-1,",", end="")
    else:
        print(i,end="")
    i=i+1
    
    
n=100
i=0
while i<=n:
    if i%2==0:
        print(i*-1,)
    if i%2!=0:
        print(i)
    i+=1