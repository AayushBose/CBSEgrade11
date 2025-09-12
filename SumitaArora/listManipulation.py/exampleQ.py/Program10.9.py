"""Write a program to find the minimum element from a list of elements along with its index in the list."""
list = eval(input("Enter the list"))
a = min(list)
i = list.index(a)
print("The minimum number is ",a,"at index position",i)