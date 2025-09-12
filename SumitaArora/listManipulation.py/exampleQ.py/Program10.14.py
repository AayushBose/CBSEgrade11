#Write a program to check if the maximum element of the list lies in the first halp of the list or in second half
list = eval(input("Enter a list"))
s = max(list)
length = len(list)/2
if list.index(s)<length:
    print("The number lies in first half")
else:
    print("The number lies in second half")
