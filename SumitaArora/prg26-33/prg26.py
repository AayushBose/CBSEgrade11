"""Ask the user to enter a list of strings. Create a new list that contains only those strings 
which start with a vowel."""
strings = input("Enter a list of strings separated by spaces: ").split()
vowel_strings = []

for s in strings:
    if s[0].lower() in "aeiou":
        vowel_strings.append(s)

print("Strings that start with a vowel:", vowel_strings)
