n=int(input("Enter the number to find its sum for its digit:"))
sum=0
while n>0:
    sum+=(n%10)*(n%10)*(n%10)
    n=n//10
print(sum)