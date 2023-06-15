import random

def play():
    print("Rock Paper Scissors Game")
    user = input('Enter r for rock, p for paper, s for scissors : ')
    computer = random.choice(['r','p','g'])

    if(user == computer):
        return("It's a tie !")
    else:
        if(is_win(user,computer)):
            return("You won !")
        return("You lost !")
            
def is_win(user,computer):
    if((user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p')):
        return(True)
    return(False)

print(play())
