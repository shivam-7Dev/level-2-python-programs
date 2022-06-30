n=int(input("Enter number to check for prime:"))
cont=2
while cont<n:
    if n%2==0:
        print("not prime") 
        break
    elif n%cont==0:
        print("not prime")
        cont=cont+1
        break
    else:
        print("prime")
        break