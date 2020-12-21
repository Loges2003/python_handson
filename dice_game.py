import random

def roll_dice():
    lst = 0
    while True:
        print('**********************************')
        roll = input("Do u want to roll the dice again?? \n*roll \n*stop \n Please enter your choice:")
        print('**********************************')
        if roll == 'roll':
            rnd = random.randint(1,6)
            print("Dice outcome is :", rnd)
            lst += 1

        elif roll == 'stop':
            print('The game is stopped, your total no of roll is :', lst)
            break
        else:
            print('sorry, your choice is not valid one')



roll_dice()