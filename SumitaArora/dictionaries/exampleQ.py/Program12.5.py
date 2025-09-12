#Write a program to create a dictionary M which stores the marks of the students of class with roll numbers as the keys and marks as the values. 
# Get the numuber of students as input
n = int(input("Enter number of students"))
d={}
for i in range(n):
    r,m = eval(input("Enter roll number and marks"))
    d[r]=m
print(d)

