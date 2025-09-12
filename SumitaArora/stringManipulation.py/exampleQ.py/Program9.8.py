#WRite a program to input 2 strings> If string 1 is incontained in string 2, then create a thrid string with first four characters of string2' added with word "Restore"
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
if s1 in s2:
    s3 = s2[:4]+"Restore"
    print(s3)