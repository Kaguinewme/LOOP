#total sum between 30 t0 420 divisible by 8
i=30
sum=0
while i<=420:
    if i%8==0:
        print(i)
        sum=sum+i
    i=i+1
print("total sum",sum,end="")