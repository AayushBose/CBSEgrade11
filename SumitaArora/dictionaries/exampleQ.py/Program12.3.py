"""Write a program to cfreate a phone dictionary for all your friends and print each key value pair in separate lines."""
name = []
phone = []
d={}
n = int(input("Enter number of friends"))
for i in range(n):
    n,p = eval(input("Enter name and phone number"))
    name.append(n)
    phone.append(p)
    d.setdefault(name[i],phone[i])
for name in d:
    print(name,":",d[name])
