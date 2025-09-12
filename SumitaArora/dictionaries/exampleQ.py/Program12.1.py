"""Write a program to read roll numbers and marks of four students and create a dictionary from it having roll numbers as keys."""
rno = []
marks= []
d={}
for i in range(4):
    r,m = eval(input("Enter the roll numbers and marks"))
    rno.append(r)
    marks.append(m)
    d.setdefault(rno[i],marks[i])
print(d)