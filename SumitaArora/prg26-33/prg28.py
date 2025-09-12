"""Write a program to read a list of ‘n’ integers from the user. Create two new lists, one having 
all positive numbers and the other having all negative numbers. Print all three lists. """
l =[]
pl=[]
nl =[]
n = int(input("Enter number of integers"))
for i in range(n):
    i = int(input("Enter integer"))
    l.append(i)
for i in range(n):
    if l[i]<0:
        nl.append(l[i])
    elif l[i]>0:
        pl.append(l[i])
print(l)
print(nl)
print(pl)
