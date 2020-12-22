from tkinter import *
from tkinter import messagebox
import array as ar
import random as rand

#common function for GUI
def replace_value(obj,x):
    obj.delete("1.0", END)
    obj.insert(END, x)

class Hangman:
    #function
    def process(self, l):
        print(l)
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

    def __init__(self):
        # List intialization
        self.wrong_guess = []



        #guess word intializtion
        self.word = self.choose_rand_word()

        self.w = self.word.__len__()
        self.list = ['_'] * self.w

        self.gui = Tk()

        # Counter intialization
        self.max_guess = self.w + 4
        self.guess_counter = 0

    def choose_rand_word(self):
        word_list = ['ATTRACT', 'APPLE', 'RENDEZVOUS', 'COMMITMENT']
        return word_list[rand.randint(0, len(word_list) - 1)]


    def button_build(self, y=200):
        x = 50

        for i in range(0, 26):
            charc = chr(65+i)#A-Z
            btn = Button(self.gui, text=charc, font='arial 8', command=lambda c=charc: self.process(c))
            btn.place(x=x, y=y)
            x += 25
            if i == 13:
                x =73
                y += 35


    def build(self):
        gui = self.gui
        gui.geometry('500x300')
        gui.title('Hangman\'s game')

        self.res = Text(gui, height=1, width=20)
        Label(gui, text='Word Length', font="arial 8").place(x=10,y=100)
        self.len = Text(gui,height=1, width = 3)

        Label(gui, text='Guess Left', font="arial 8").place(x=110,y=100)
        self.guess_no = Text(gui, height=1, width=3)

        Label(gui, text='Wrong Moves', font="arial 8").place(x=210,y=100)
        self.wrng_move = Text(gui, height = 1, width = 11)

        #to show word length in GUI
        self.len.place(x=80,y=100)
        self.len.insert(END, self.w)

        #to show no. of moves left in GUI
        self.guess_no.insert(END,self.max_guess )
        self.guess_no.place(x=172,y=100)

        # to show wrong gusses in GUI
        self.wrng_move.place(x=310, y=100)
        self.res.place(x=120, y=50)
        self.res.insert(END,self.list)

        self.button_build()
        gui.mainloop()

#object creation for class
hm = Hangman()
hm.build()





