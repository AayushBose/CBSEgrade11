"""Write a program to perform various list operations using menu driven operations. 
a. Add element             c.Delete element e. Display list 
b. Modify element        d. Add another list f. Exit """
l = eval(input("Enter a list: "))
print("---MENU---")
while True:
    print("a. Add element\nb. Modify element\nc.Delete element\nd. Add another list\ne. Display list\nf. Exit")
    ch = input("Enter choice: ")
    if ch == "a":
        n = input("Enter element to be added")
        l.append(n)
    if ch == "b":
        n = input("Enter element to be modified")
        i = int(input("Enter index at which element is to be modified"))
        l[i]=n
    if ch == "c":
        n = input("Enter element to be deleted")
        l.remove(n)
    if ch == "d":
        l1 = eval(input("Enter list to be added"))
        l.extend(l1)
    if ch == "e":
        print(l)
    if ch == "f":
        break


