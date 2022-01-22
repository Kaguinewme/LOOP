# A
# B B
# C C C
# D D D D
# E E E E E

i=0
while i<5:
    print((chr(65+i)+" ")*(i+1))
    i=i+1
    
    
## nested 
   
i=65
while i<=69:
    j=65
    while j<=i:
        print(chr(i), end=" ")
        j=j+1
    i=i+1
    print()
    
## for loop
for i in range(65,70):
    for j in  range (65,i+1):
        print(chr(i),end=" ")
    print()