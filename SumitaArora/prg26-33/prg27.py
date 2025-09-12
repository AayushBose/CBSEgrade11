"""Write a program to create a nested tuple to store marks of three subjects for five students. 
Compute the total marks and average obtained by each student. """
l = []
for i in range(5):
    marks = input(f"Enter marks for student {i+1}: ").split()
    l.append(tuple(marks))
print(l)
for i in range(5):
    sum = 0
    for j in range(3):
        sum+=int(l[i][j])
    avg = sum/3
    print("Average of marks for student",i+1,avg)
