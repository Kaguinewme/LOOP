
       
# n=int(input("enter the number"))
# temp=n
# reversed=0
# while temp>0:
#     remainder=temp%10 
#     temp =temp//10
#     reversed=reversed*10+remainder
# if n==reversed:
#     print("palindrone")
# else:
#     print("not")

n=int(input("enter the number"))
temp=n
reversed=0
while temp>0:
    remainder=temp%10 
    temp =temp//10
    reversed=reversed*10+remainder
print(reversed)
   