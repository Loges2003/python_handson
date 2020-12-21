'''from numpy import *



ar2 = logspace(1,50,5)
print(ar2)
print('%.2f' %ar2[2])

ar1= linspace(0,49)

print(ar1)

arr = array([4, 6, 7, 5, 8, 1.3457834549387543987638475],long)

print(arr)
print(arr.dtype)

n = int(input('Enter the value to find:'))

k = 0
for i in arr:
    if i == n:
        print('the position is:', k)
        break
    k += 1
else:
    print('the entered value is not present in the array')

'''

a=[10,5,6,7,4]


def func():
    print(globals()['__cached__'])
    #for i in globals()['__spec__']:  #__name____doc____package____loader____spec____annotations____builtins____file____cached__afunc
       # print(i, end='')

    #x = globals()['a']
    #print(x)
#func()

nums = [2,5,6,7,8,9]

#even = [nums for i in nums i%2 == 0]

'''it = iter(nums)

print(it.__next__())
print(it.__next__())

print(next(it))'''

#ff = list(map(lambda n : n*2, nums))

#print(ff)
#print(ff.__next__())
#print(ff.__next__())
#print(ff.__dir__())
'''
n = int(input('Enter range for fibnocci series:'))
list = [0,1]
a=0
b=1

for i in range(0,n-2):
    #c = a+b
    a,b = b,a+b
    if b <= n:
        list.append(b)
    else:
        break

print(list)

fact = int(input('Enter a value to find its factorial:'))
a=1
for i in range(1,fact+1):
    a= a*i

print(a)'''

import sys
a=1
def fact(n):
    if n == 1:
        return 1
    res = n * fact(n - 1)
    return res
print(fact(5))





