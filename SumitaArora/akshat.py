#To check if a number is palindrome
n = int(input("Enter a number: "))
t = n
r = 0
num=0
while t>0:
    r = t%10
    num = num*10+r
    t=t//10
if num == n:
    print("Number is palindrome")
else:
    print("Number is not palindrome")

