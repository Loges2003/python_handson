'''i = 1

while i <= 5:
    j = i
    while j >= 1:
        print('*', end='')
        j-=1

    i+=1
    print()

'''

'''class A:
    def show(self):
        print("in a")


class B(A):
    def show(self):
        print("in b")

a1 = B()
a1.show()

a=5
b=0
try:
   a/b
except Exception as e:
    print(e)
'''
from threading import *
from time import sleep

class A(Thread):
    def run(self):
        for i in range(10):
            print('hi')
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(10):
            print('hello')
            sleep(1)
t1 = A()
t2 = B()

t1.start()
sleep(0.2)
t2.start()

print('bye')
