#find the average weights of 11 people and find whether the average is multiple of 5
i=0
sum=0
while i<11:
    i=i+1
    weight=int(input("enter the number"))
    sum=sum+weight
print(sum)
avg=sum/11
print(avg)
if avg%5==0:
    print(avg,"divisible by 5")
else:
    print(avg,"not divisible")