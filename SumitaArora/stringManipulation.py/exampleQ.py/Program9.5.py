#Write a program that asks a user for a usuername and a code. Ensure that the user doesnt use the username as part of their code.
username = input("Etnr a username: ")
code = input("Enter a code: ")
if username in code:
    print("Username cannot be a part of the code")
print("Thank you")