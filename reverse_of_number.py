from audioop import reverse


n=int(input("Enter number to find the reverse:"))
rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
print(rev)