n=int(input("Enter number to check for palindrome:"))
number=n
rev=0
while n>0:
    rev=rev*10+(n%10)
    n=n//10
if rev==number:
    print("number is palindrome")
else:
    print("number is not palindrome")