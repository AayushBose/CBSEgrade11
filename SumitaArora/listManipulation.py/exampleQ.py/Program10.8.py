'''Write a program that inputs a list, replicates it twice and then prints the sorted list in ascending and descending order.'''
s = eval(input("Enter a list :"))
s = s*2
s.sort()
print("IN ascending order: ", s)
s.sort(reverse=True)
print("In descending order: ", s)