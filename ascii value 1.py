# A A A A A
# B B B B B
# C C C C C
# D D D D D
# E E E E E 
n= int(input("enter the rows"))
i=65
while i<=69:
    j=1
    while j<=n:
        print(chr(i), end=" ")
        j+=1
    print()
    i=i+1