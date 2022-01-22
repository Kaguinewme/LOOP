#wrie a code that calculates the sum of those no. from 30 to 420 which are multiples
# of 8 that means those no come in the table of 8
i=30
sum=0
while i<=420:
    if i%8==0:
        print(i)
        sum=sum+i 
    i=i+1 
print("total sum", sum,end="")      