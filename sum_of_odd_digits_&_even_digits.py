n=int(input("Enter number to find the sum of odd digits and even digits:"))
sum_even=0
sum_odd=0
while n>0:
    if (n%10)%2==0:
        sum_even+=n%10
        n=n//10
    else:
        sum_odd+=n%10
        n=n//10
print("Even sum is:",sum_even)
print("odd sum is:",sum_odd)

