n=int(input("Enter the number to find its sum for its digit:"))
sum=0
while n>0:
     sum=sum+n%10
     n=n//10
print(sum)
# print(9//10) output will be 0
