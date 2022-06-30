n=int(input("Enter number to check for prime:"))
cont=0
i=1
while i<=n:
    if n%i==0:
        cont=cont+1
    i=i+1
    
print(cont)
if cont==2:
    print("number is prime")
else:
    print("number is not prime")