import os

USER_DATA_FILE = "user_data.txt"

def load_users():
    users = {}
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                users[username] = password
    return users

def user(username, password):
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username}:{password}\n")

def register(userlist):
    print("=== User Registration ===")
    username = input("Enter a username: ")
    if username in userlist:
        print("Username already exists! Please choose a different one.")
        return None, None
    password = input("Enter a password: ")
    user(username, password)
    userlist[username] = password
    print("Registration successful!")
    return username, password

def login(userlist):
    username = input("Enter your usuername: ")
    if username not in userlist:
        print("Username is not registered")
        return None
    password = input("Enter your password: ")
    if userlist[username]==password:
        print("Login successful!")
        return username
    else:
        print("Password incorrect!")
        return None
    
def game():
    print("The game starts!")
    quiz = [
        {"question":"What is the capital of France ","options":["Paris","Berlin","London","Oslo"],"answer":"Paris"},
        {"question":"What is the capital of Russia ","options":["St. Petersburg","Delhi","New York","Moscow"],"answer":"Moscow"},
        {"question":"What is the capital of China ","options":["San Francisco","Shanghai","Wuhan","Beijing"],"answer":"Beijing"},
        {"question":"What is the capital of India ","options":["Mumbai","Bengaluru","Delhi","Kolkata"],"answer":"Delhi"}]
    score = 0
    for q in quiz:
        print(q["question"])
        print(q["options"])
        answer = input("Enter the answer: ")
        if q["answer"]==answer:
            score = score+1
    print("Your total score is", score,"out of 4")    

def main():
    print("Welcome to the Quiz Game!")
    userlist = load_users()  

    choice = input("Do you want to (1) Register or (2) Login: ")
    
    if choice == '1':
        username, password = register(userlist)
        if username:
            game()
    elif choice == '2':
        username = login(userlist)
        if username:
            game()
    else:
        print("Invalid choice! Exiting.")
        return
main()
