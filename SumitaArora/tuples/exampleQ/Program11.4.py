#Write a program to print a tuple's first three and last three elements in the following manner:
'''
1st element, last element
2nd element, 2nd last element
3rd element, 3rd last element'''
t = eval(input("Enter the tuple"))
print(t[0],t[-1])
print(t[1],t[-2])
print(t[2],t[-3])