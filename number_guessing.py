#https://www.upgrad.com/blog/python-projects-ideas-topics-beginners/
# Ex:2 Number Guessing

print("Guess a number between 1- 100 in 5 guesses")

a = 45

for i in range(5):

    num = int(input("Enter the number:"))

    if num == a:
        print('Great, You win!!!')
        break

    elif num <= 40:
        print('Your Guess too less than the hidden number')

    elif num >= 50:
        print('Your Guess is too far than hidden number')

    else:
        print('you were almost near!!')
else:
    print("your Chance is over")
