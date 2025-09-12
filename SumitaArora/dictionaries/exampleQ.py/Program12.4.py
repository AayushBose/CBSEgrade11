"""Given a dictionary M which stores the marks of the students of classs with roll numbers as the keys and marks as the alues. 
Write a program to check if anyone has scored marks as 89.9"""
rno = []
marks= []
d={}
for i in range(4):
    r,m = eval(input("Enter the roll numbers and marks"))
    rno.append(r)
    marks.append(m)
    d[rno[i]]=marks[i]
print(d)
if 89.9 in d.values():
    print("Yes, someone has scored 89.8")
else:
    print("No, no one has scored 89.9")