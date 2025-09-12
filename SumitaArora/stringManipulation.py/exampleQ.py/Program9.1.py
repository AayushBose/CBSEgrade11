#Program to read a string and display it in reverse order-display one character at a time, Do not create a reverse string just reverse the order of the string
string = input("Enter a string: ")
print("The string in reverse order is ")
for i in range(-1,(-len(string)-1),-1):
    print(string[i])
