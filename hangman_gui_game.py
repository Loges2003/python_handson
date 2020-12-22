from tkinter import *
from tkinter import messagebox

gui = Tk()
gui.geometry('500x300')
gui.title('Hangman\'s game')

res = Text(gui, height=1, width=15)
Label(gui, text='Word Length', font="arial 8").place(x=10,y=100)
len = Text(gui,height=1, width = 3)

Label(gui, text='Guess Left', font="arial 8").place(x=110,y=100)
guess_no = Text(gui, height=1, width=3)

Label(gui, text='Wrong Moves', font="arial 8").place(x=210,y=100)
wrng_move = Text(gui, height = 1, width = 11)

#common function for GUI
def replace_value(obj,x):
    obj.delete("1.0", END)
    obj.insert(END, x)

# List intialization
wrong_guess = []
list = ['_','_','_','_','_','_','_' ]


# Counter intialization
max_guess = 7
guess_counter = 0

#guess word intializtion
word = 'ATTRACT'
w = word.__len__()
print(w)

#function
def process(l):
    ind = 0
    globals()['guess_counter'] += 1
    mg = globals()['max_guess']
    guess_left = mg - globals()['guess_counter']
    word = globals()['word']

    for ltr in word:
        if ltr == l:
            list[ind] = l

        ind += 1
    else:
        if l not in word:
            wrong_guess.append(l)

    print(list)
    # to show gusses in GUI
    replace_value(res, list)

    print(wrong_guess)
    # to show wrong gusses in GUI
    replace_value( wrng_move, wrong_guess)
    replace_value(guess_no, guess_left)

    #To check for no of guesses
    if guess_counter < mg:
        if '_' in list:
            pass
        else:
            print('you win')
            messagebox.showinfo(title="Success",message="You win")
            gui.quit()
    else:
        print('you have exceed the limit')
        messagebox.showinfo(title="Please try again", message="You have Exceeded the limit... \nThe word is "+word)
        gui.quit()








Button(gui, text = 'A',font='arial 8', command = lambda : process('A')).place(x=50,y=200)
Button(gui, text = 'T',font='arial 8', command = lambda : process('T')).place(x=70,y=200)
Button(gui, text = 'R',font='arial 8', command = lambda : process('R')).place(x=90,y=200)
Button(gui, text = 'C',font='arial 8', command = lambda : process('C')).place(x=110,y=200)
Button(gui, text = 'Z',font='arial 8', command = lambda : process('Z')).place(x=130,y=200)
Button(gui, text = 'M',font='arial 8', command = lambda : process('M')).place(x=150,y=200)



#to show word length in GUI
len.place(x=80,y=100)
len.insert(END, w)

#to show no. of moves left in GUI
guess_no.insert(END,max_guess )
guess_no.place(x=172,y=100)

#To show alert message
# to show wrong gusses in GUI
wrng_move.place(x=310, y=100)
res.place(x=120, y=50)


gui.mainloop()








