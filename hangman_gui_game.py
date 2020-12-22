from tkinter import *
from tkinter import messagebox

#common function for GUI
def replace_value(obj,x):
    obj.delete("1.0", END)
    obj.insert(END, x)

class Hangman:
    #function
    def process(self, l):
        ind = 0
        self.guess_counter += 1
        guess_left = self.max_guess - self.guess_counter

        for ltr in self.word:
            if ltr == l:
                self.list[ind] = l

            ind += 1
        else:
            if l not in self.word:
                self.wrong_guess.append(l)

        # to show guesses in GUI
        replace_value(self.res, self.list)

        # to show wrong gusses in GUI
        replace_value( self.wrng_move, self.wrong_guess)
        replace_value(self.guess_no, guess_left)

        #To check for no of guesses
        if self.guess_counter < self.max_guess:
            if '_' in self.list:
                pass
            else:
                print('you win')
                messagebox.showinfo(title="Success",message="You win")
                self.gui.quit()
        else:
            print('you have exceed the limit')
            messagebox.showinfo(title="Please try again", message="You have Exceeded the limit... \nThe word is "+self.word)
            self.gui.quit()

    def init(self):
        # List intialization
        self.wrong_guess = []
        self.list = ['_','_','_','_','_','_','_' ]

        # Counter intialization
        self.max_guess = 7
        self.guess_counter = 0

        #guess word intializtion
        self.word = 'ATTRACT'
        self.w = self.word.__len__()
        self.gui = Tk()

    def build(self):
        gui = self.gui
        gui.geometry('500x300')
        gui.title('Hangman\'s game')

        self.res = Text(gui, height=1, width=15)
        Label(gui, text='Word Length', font="arial 8").place(x=10,y=100)
        self.len = Text(gui,height=1, width = 3)

        Label(gui, text='Guess Left', font="arial 8").place(x=110,y=100)
        self.guess_no = Text(gui, height=1, width=3)

        Label(gui, text='Wrong Moves', font="arial 8").place(x=210,y=100)
        self.wrng_move = Text(gui, height = 1, width = 11)

        Button(gui, text = 'A',font='arial 8', command = lambda : self.process('A')).place(x=50,y=200)
        Button(gui, text = 'T',font='arial 8', command = lambda : self.process('T')).place(x=70,y=200)
        Button(gui, text = 'R',font='arial 8', command = lambda : self.process('R')).place(x=90,y=200)
        Button(gui, text = 'C',font='arial 8', command = lambda : self.process('C')).place(x=110,y=200)
        Button(gui, text = 'Z',font='arial 8', command = lambda : self.process('Z')).place(x=130,y=200)
        Button(gui, text = 'M',font='arial 8', command = lambda : self.process('M')).place(x=150,y=200)

        #to show word length in GUI
        self.len.place(x=80,y=100)
        self.len.insert(END, self.w)

        #to show no. of moves left in GUI
        self.guess_no.insert(END,self.max_guess )
        self.guess_no.place(x=172,y=100)

        # to show wrong gusses in GUI
        self.wrng_move.place(x=310, y=100)
        self.res.place(x=120, y=50)

        gui.mainloop()

#object creation for class
hm = Hangman()
hm.init()
hm.build()





