"""Write a program that asks the user to input a number a list to be appended to an existing list.
Whether the user enetrs a single number or a list of numbers, the program should append the list accoridngly.
"""
list = eval(input("Enter a list: "))
n = eval(input("Enter number to be added to the list"))
if type(n)==type([]):
    list.extend(n)
elif type(n)==type(1):
    list.append(n)
print(list)
