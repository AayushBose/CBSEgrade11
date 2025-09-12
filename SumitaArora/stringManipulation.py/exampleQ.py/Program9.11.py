#Write a program that reads a line and a substring. It should then display the number of occurences of the given substring in the line.
s = input("Enter a string")
s1 = input("Enter substring")
count=start= 0
length = len(s)
lensub = len(s1)
while True:
    pos = s.find(s1,start)
    if pos!=-1:
        count+=1
        start = pos+lensub
    else:
        break
print("The number of occurences of the substring in the string is: ",count)