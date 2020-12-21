
'''
def search(list, n):
    l = len(list)
    for i in range(l):
        if list[i] == n:
            return i+1

    return -1

list=[4,6,8,2,9,1]
n = 2

pos = search(list,n)
print(type(pos))
if pos != -1:
    print('found ',pos)
else:
    print('not found')

'''


'''
pos = -1

def search(list,n):
    i = 0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i += 1
        #print(i)

    return False



list=[4,6,8,2,9,1]
n=8

if search(list,n):
    print('Found', pos)
else:
    print('not found')



list = [3,5,8,9,11,12]
n = 10
lower = 0
upper = len(list)-1

while lower <= upper:
    mid = ((lower+upper)//2)
    mv = list[mid]

    if mv == n:
        print('found @ mid',mid)
        break
    elif mv > n :
        upper = mid - 1
    elif mv < n:
        lower = mid + 1

else:
    print('Not found')

print('Bye')

b = [5,8,3,1,6]

b.sort()
print(b)'''

'''
class Mmath:

    def bubble_sort(self,list):

        ub = len(list)-1

        for i in range(ub):
            j=0

            while j < ub:#(ub-i):
                if list[j] > list[j+1]:
                    t= list[j]
                    list[j]= list[j+1]
                    list[j+1] = t

                j += 1





list= [10,5,7,9,13,20,2]

c=Mmath()

c.bubble_sort(list)
print(list)



j = 0
    for j in range(i):
        print(list[j], end='')
        if list[j] > list[j+i]:
            t = list[j]
            list[j] = list[j+1]
            list[j+1]=t
            j += 1

        i += 1

list =[10,5,7,9,13,20,2]

ub = len(list)

for i in range(ub):
    if list[i-1]> list[i+1]:
        temp = list[i]
        list[i] = list[i+1]
        list[i+1] = temp





def a(name,**kwargs):

    for i,j in kwargs.items():
        print(i)
        print(j)

a('navin', age = '20', city ='mumbsi', desig='manager')

x='5'
y='1'

#x= x ^ y
##y= x ^ y
#x = x ^ y

x,y = y,x
print('x is',x, '\ny is',y )'''

import math

def is_prime(a):
    math_div = math.floor(math.sqrt(a))

    for i in range(2, math_div+1):
        division = a % i

        if division == 0:
            print('not prime')
            break
    else:
        print('prime')

is_prime(2222)


'''def prime(a):
    a=int(a)
    flag = True

    for i in range(2,a):
        rem = a % i
        if rem == 0:
            flag=False
            break

    return flag

    #print('the given no. is prime')

if prime(127)==True:
    print('the given no. is prime')
else:
    print('the given no. is not prime')

'''

'''
from array import *

vals = array('i', [4,5,6,7,8])

new = array('i', [i*i for i in vals ])
b = [5.8,6.6,9]

vals.extend(b)

print(vals)
print(new) '''

from array import *

arr = array('i',[4,6,7,5,8,1])

n = int(input('Enter the value to find:'))

for i in len(arr):
    if arr[i] == n:
        print('the position is:',i)
        break
    