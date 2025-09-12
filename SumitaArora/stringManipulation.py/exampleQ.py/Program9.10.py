"""Write a program that reads a line and prints its statistics like:
Number of uppercase letters
Number of alphabets
Number of symbols
Number of lowercase letters
Number of digits
"""
line = input("Enter a string")
uCount=aCount=lCount=dCount=sCount=0
for ch in line:
    if ch.isupper():
        uCount+=1
    if ch.islower():
        lCount+=1
    if ch.isalpha():
        aCount+=1
    if ch.isdigit():
        dCount+=1
    if ch.isalnum()!=True:
        sCount+=1
print("Number of uppercase letters", uCount)
print("Number of alphabets", aCount)
print("Number of symbols", sCount)
print("Number of lowercase digits", lCount)
print("Number of digits", dCount)