#https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
# Ex:2 Number Guessing
import random
print("Guess a number between 1- 100 in 5 guesses")

#a = 45
a = random.randint(1,100)

for i in range(5):

    num = int(input("Enter the number:"))
    diff = num-a


    if num == a:
        print('Great, You win!!!')
        break

    elif diff <= -5:
        print('Your Guess too less than the hidden number')

    elif diff >= 5:
        print('Your Guess is too far than hidden number')

    else:
        print('you were almost near!!')
else:
    print("your Chance is over")
    print('The number is :',a)
