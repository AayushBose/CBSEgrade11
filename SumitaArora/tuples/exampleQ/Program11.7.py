"""
Write a program to input a tuple and create 2 new tuples from it, one containing its every 3rd element in reverse order, starting from the last element another 
containing every alternate elements lying between 3rd to 9th elements"""
tp = eval(input("Enter the tuple"))
tp1 = tp[::-3]
tp2 = tp[2:8:2]
print(tp1)
print(tp2)