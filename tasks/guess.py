import random

def comp_number(x):
    low = 1
    high = x
    feedback =''
    while feedback != 'c':
        if low != high:
            num = random.randint(low, high)
        if low == high:
            num = low
        feedback = input(f'Is {num} your number. Press (h) if it is too high,\
(l)- too low and (c) if it is correct ')
        if feedback == 'h':
            high = num -1
        if feedback == 'l':
            low = num +1
    print(f'Yay, congrats the computer. I have guessed the number,{num}, correctly. What a wonderful computer I am. You are probably jelous right now')
comp_number(100)
