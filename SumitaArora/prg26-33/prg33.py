"""Write a program to repeatedly ask user to enter a team name and how many games the 
team has won or lost. 
a) Using dictionary, allow the user to enter team name and print out the teams win percentage. 
b) Using it to create a list whose entries are the number of wins of each team. 
c) Using dictionary create a list of all teams having winning records. 
"""
l = []
l1= []
teams = {}
while True:
    teamname = input("Enter team name or type stop: ")
    if teamname.lower()=="stop":
        break
    wins = int(input("Enter number of wins: "))
    loss = int(input("Enter number of loss: "))
    wp = wins/(wins+loss)
    teams[teamname]={"wins":wins,"loss":loss,"win percentage":wp}
print(teams)
print(teams.items())
name = input("Enter team name: ")
print(teams[name])

for i,item in teams.items():
    l.append(item["wins"])
print("Wins of each teams are as follows:",l)

for i,item in teams.items():
    if item["wins"]>item["loss"]:
        l1.append(i)
print("Winning record teams are as follows:",l1)

