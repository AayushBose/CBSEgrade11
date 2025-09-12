#Write a program to input an integer and check if it contains the number 0 in it
t = int(input("Enter an integer: "))
string = str(t)
if '0' in string:
    print("The number contains 0")
else:
    print("The number does not contain 0")
    