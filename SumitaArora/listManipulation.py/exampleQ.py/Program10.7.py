'''
Write a program that displays options for inserting or deleting elements in a list. If the user chooses a deletion option,
display a submenu and ask if element is to be deleted with value or by using its position or a list slice is to be deleted
'''
val = [1,2,3,4]
while True:
    print("-----MAIN MENU-----")
    print(" 1. Insert \n 2. Delete \n 3. Exit ")
    ch = int(input("Enter choice number"))
    if ch == 1:
        item = int(input("Enter item: "))
        pos = int(input("Insert element at which position: "))
        index = pos-1
        val.insert(index,item)
        print("The list is: ",val)
    elif ch == 2:
        print("----SUBMENU----")
        print("1. delete by value")
        print("2. delete by position")
        print("3. delete list slice")
        c = int(input("Enter your choice: "))
        if c == 1:
            value = int(input("Enter the value: "))
            val.remove(value)
            print("The updated list is :",val)
        if c == 2:
            posi = int(input("Enter position at which number is to be deleted: "))
            val.pop(posi)
            print("Updated list is: ",val)
        if c == 3:
            start = int(input("Enter starting position: "))
            end = int(input("Enter ending position"))
            del(val[start-1:end])
            print("Updated list is :",val)
    elif ch==3:
        break