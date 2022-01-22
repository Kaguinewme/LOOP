
print("enter two number",end="")
n=int(input("enter the number"))
n1=int(input("enter the number"))

if n>n1:
    hcf=n
else:
    hcf=n1
while True:
    if n%hcf==0 and n1%hcf==0:
       break 
    
    else:
        hcf=hcf-1
print("\nHCF (" + str(n) + "," + str(n1) + ")=",hcf)


    
