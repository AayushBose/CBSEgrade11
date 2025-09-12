#Write a program that inputs a string that contains a decimal number and prints out the decimal part of the number. FOr instancem if 515,8059 is given, the program should print out 8059
a = input("Enter a number")
t = a.index(".")
s = a[t+1:]
print("The decimal part of the number is",s)