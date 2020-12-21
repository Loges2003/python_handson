from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('DataFlair-Mad Libs Generator')
Label(root, text='Mad Libs Generator \n Have Fun!', font='arial 20 bold').pack()  #pack function is used to display this, center aligned from the top
Label(root, text = 'Click Any One :', font = 'arial 15 bold').place(x=40, y=80)



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


Button(root, text='  ZOO  ', font='arial 15', command=story1).place(x=120, y =140)
Button(root, text='Dream', font='arial 15', command=story2).place(x=120, y =210)

root.mainloop()