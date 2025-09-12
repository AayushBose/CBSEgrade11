#Write a program that asks a user for a username and a pcode. Make sure that pcode does not contain username and matches 'Trident111'
username = input("Enter a username: ")
pcode = input("Enter a pcode: ")
if username not in pcode and pcode == 'Trident111':
    print("Your code is valid")
else:
    print("Your code is invalid")