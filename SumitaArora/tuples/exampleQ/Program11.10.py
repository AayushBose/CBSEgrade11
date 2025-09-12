"""
Write a program to input a 4 element tuple and unpack it to four variables. Then recreate the tuple with elements wapped as 1st element with 33rd element and 2nd with 4th element."""
t = eval(input("Enter 4-element tuple"))
a,b,c,d=t
t1 = (c,d,a,b)
print(t1)