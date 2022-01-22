#p
#p y
#p y t
#p y  t h
#p y t h o
#p y t h o n

string=input("enter the string")
length=len(string)
row=0
while row<length:
    col=0
    while col<=row:
        print(string[col],end=" ")
        col+=1
    row+=1
    print()
    
# for loop
str=input("enter the string=")
length=len(str)
for row in range (length):
    for col in range(row+1):
        print(str[col],end="")
    print()