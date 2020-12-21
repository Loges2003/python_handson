
def story1():
    name = input('Please enter friend name: ')
    animal = input('Please enter animal name: ')
    food = input('Please enter any food: ')
    place = input('Please enter a location: ')

    print('I went along with my friend ', name, "to a zoo located at ", place,
          '. We saw many animals, out of all i liked the ', animal,
          ' most. We then went to a nearby restaurant and ate ', food)

def story2():
    name = input('Please enter friend name: ')
    animal = input('Please enter animal name: ')
    place = input('Please enter a location: ')

    print('One night I dreamed of going with ', name, "to a forest located at ", place,
          '. We saw many animals, out of all the ', animal,
          ' started chasing us.Out of fear I woke up then')


print('*****************************')
print("Madlib Game. \n1.Zoo \n2.Dream")
print('*******************************')

choice = int(input('Enter your choice'))


if choice ==1:
    story1()
elif choice == 2:
    story2()
else:
    print('wrong choice, please enter valid choice')