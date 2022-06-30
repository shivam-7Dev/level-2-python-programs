from concurrent.futures import process


n=int(input("Enter number to pind product of its digit:"))
product=1
while n>0:
    product=product*(n%10)
    n=n//10
print("product of the entered digits is:",product)