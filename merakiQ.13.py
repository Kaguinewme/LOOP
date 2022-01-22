#Take an integer input in a variable named n. Take user input as many times as the value of n.

#Finally, print the sum of all those numbers which you have taken as an input.


i=1
sum=0
n=int(input("enter the number"))
while i<=n:
    num=int(input("enter the required number"))
    sum=sum+num
    i=i+1
print(sum)