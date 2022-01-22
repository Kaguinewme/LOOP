# n=int(input("enter the number"))
# temp=n
# sum=0
# while n>0:
#     digit=n%10
#     n=n//10
#     fact=1
#     total=total+1
# if total==temp:
#     print("strong number")
# else:
#     print("not a strong number")

# n=int(input("enter the number"))
# temp=n
# sum=0
# while n>0:
#     r=n%10
#     fact=1
#     for i in range(1,r+1):
#         fact=fact*i
#     sum=sum+fact
#     n=n//10
# if sum==temp:
#     print("strong number")
# else:
#     print("not a strong no")


n=int(input("enter the nuber"))
temp=n
sum=0
while n>0:
    i=1
    fact=1
    remainder=n%10
    while i<=remainder:
        fact=fact*i
        i=i+1
    sum=sum+fact
    n=n//10
if sum==temp:
    print("strong no") 
else:
    print("not")   
    
    


 
    
    
    