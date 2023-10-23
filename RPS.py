import random

user_win = 0
sys_win = 0

choices = ["rock", "paper", "scissors"]

while True:
    user = input(f"Rock Paper or Scissors? or do not wanna play anymore- 'no more'? :> ").lower()
    if user == "no more":
        break

    if user not in choices:
        continue
    
    rdm = random.randint(0, 2)
    sys = choices[rdm]
    print(f"Computer chose {sys}.")
    
    if user == "rock" and sys == "scissors":
        print(f"{user} beats {sys}, you won!")
        user_win += 1
    
    elif user == "paper" and sys == "rock":
        print(f"{user} beats {sys}, you won!")
        user_win += 1
    
    elif user == "scissors" and sys == "paper":
        print(f"{user} beats {sys}, you won!")
        user_win += 1

    elif user == sys:
        print(f"You both chose {user}, so no one won this round")

    else:
        print(f"{sys} beats {user}, you lose!")
        sys_win += 1

print(f"You won {user_win} times and System won {sys_win}")
print("Tata~")
