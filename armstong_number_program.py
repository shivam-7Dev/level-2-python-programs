n=int(input("Enter the number to check if it is armstrong or not:"))
number=n
sum=0
while n>0:
    sum+=(n%10)*(n%10)*(n%10)
    n=n//10
if  sum==number:
    print("number is armstrong")
else:
    print("number is not armstrong")



### testing commit change