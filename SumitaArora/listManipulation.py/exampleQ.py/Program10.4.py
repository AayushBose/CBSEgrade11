#Program to create a 2D list
Lst = list()
r = int(input("Enter number of rows"))
c = int(input("Enter number of columns"))
for i in range(r):
    row = []
    for j in range(c):
        elem = int(input("Element"+str(i)+str(j)+": "))
        row.append(elem)
    Lst.append(row)
print("2D list created is: ", Lst)