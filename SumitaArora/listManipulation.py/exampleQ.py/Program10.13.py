"""Write a program to find frequences of all elements of a list. Also, print the list of unique elements in the list and duplicate elements in the given list"""
list = eval(input("Enter the list"))
list2 = []
uniq = []
duplicates = []
for i in range(0,len(list)):
    count = 0
    element = list[i]
    for j in range(0,len(list)):
        if element == list[j] and element not in list2:
            count = count+1
    if count == 1:
        uniq.append(element)
    elif count!=1 and element not in list2:
        duplicates.append(element)
    if element not in list2:
        list2.append(element)
        print("The frequency of ",element,"is",count)
print("The unique elements list is :",uniq)
print("The duplicates elements list is: ",duplicates)