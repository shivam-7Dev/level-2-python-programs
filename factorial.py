n=int(input("Enter number to find factorial:"))
fact=1
count=1
while count<=n:
    fact=fact*count
    count=count+1
print(fact)