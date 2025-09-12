"""Create a dictionary whose keys are month names and whose values are number of days in the 
corresponding months. Perform the following: 
• Ask the user to enter a month name, and use dictionary to tell how many days are in the 
month. 
• Print out all of the months with 31 days. 
• Print out all of the keys in alphabetical order.
"""
d1 = {"january":31,"february":28,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
month = input("Enter month name: ").lower()
print("Number of days in",month,"are",d1[month])
print("\nMonths with 31 days are as follows:")
for keys in d1:
    if d1[keys]==31:
        print(keys)
print("\nMonths arranged in alphabetical order as follows:",sorted(d1.keys()))