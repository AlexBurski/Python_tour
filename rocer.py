import random

def play ():
    while True:
        computer = random.choice(['r','p','s'])
        user = input("Print 'r' for rock, 'p' for paper and 's' for scissors 'stop' if you want to quit")
        if user == 'stop':
            break
        elif user == computer:
            return print("It's a tie")
        elif is_win(user,computer):
            return print('You won')
        return print('You lost')
    #r>s p>r s>p
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or(player == 'p' and opponent == 'r') or (player == 's' and opponent =='p'):
        return True

play()

while True:
    computer = random.choice(['r', 'p', 's'])
    user = input("Print 'r' for rock, 'p' for paper and 's' for scissors 'stop' if you want to quit")
    if user == 'stop':
        break
    elif user == computer:
        print("It's a tie")
    elif is_win(user, computer):
        print('You won')
    else:
        print('You lost')