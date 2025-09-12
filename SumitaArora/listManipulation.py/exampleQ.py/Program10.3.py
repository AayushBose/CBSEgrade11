#Write a program to create a copy of a list. In the list's copy, add 10 to its first and last elements. Then display the lists.
L1 = eval(input("Enter a list"))
L2 = L1.copy()
L2[0]+=10
L2[len(L2)-1]+=10
print(L1)
print(L2)