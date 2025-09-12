"""Write a program to accept age of employees & count the number of employees in the following 
age groups. 
a.   26-35      b.  36-45      c.  46-55 
"""
c1=c2=c3=0
n = int(input("Enter number of employees"))
for i in range(n):
    age = int(input("Enter age of the employee"))
    if age>=26 and age<=35:
        c1+=1
    elif  age>=36 and age<=45:
        c2+=1
    elif age>=46 and age<=55:
        c3+=1
print("Number of employees of age within 26-35", c1)
print("Number of employees of age within 36-45", c2)
print("Number of employees of age within 46-55", c3)
