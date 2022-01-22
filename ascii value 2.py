# A B C D E
# A B C D E
# A B C D E
# A B C D E
# A B C D E 
n= int(input("enter the rows"))
i=65
while i<=69:
    j=0
    k=ord("A")+j
    while j<n:
        print(chr(k),end=" ")
        k=k+1
        j=j+1
    print()
    i=i+1