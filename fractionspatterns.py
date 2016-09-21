"""
fractionspatterns.py
Author: Avery Wallis

This was an experiment for Math Modeling and Fractions

"""
import math
listfr = []
list2 = []
list2fr = []
list3 = []
list3fr = []
list31= []
list4 = []
list4fr = []
list5 = []
list5fr = []
list6 = []
list6fr = []
list7 = []
list7fr = []
list8 = []
list8fr = []
list9 = []
list9fr = []
list10 = []
list10fr = []
listsr2 = []
listsr2fr = []
listsr3 = []
listsr3fr = []
listsr4 = []
listsr4fr = []
listsrd2 = []
listsrd2fr = []
a = 0
b = 0
d = int(input("Largest Denominator?"))
for x in range(0,d):
    x = x
    a = 1
    b += 1
    c = a/b
    listfr.append(c)
    if b%2==0:
        list2.append(b)
        list2fr.append(c)
    if b%3==0:
        list3.append(b)
        list3fr.append(c)
    if b%3==1:
        list31.append(b)
    if b%4==0:
        list4.append(b)
        list4fr.append(c)
    if b%5==0:
        list5.append(b)
        list5fr.append(c)
    if b%6==0:
        list6.append(b)
        list6fr.append(c)
    if b%7==0:
        list7.append(b)
        list7fr.append(c)
    if b%8==0:
        list8.append(b)
        list8fr.append(c)
    if b%9==0:
        list9.append(b)
        list9fr.append(c)
    if b%10==0:
        list10.append(b)
        list10fr.append(c)
    if math.sqrt(b)==2:
        listsr2.append(b)
        listsr2fr.append(c)
    if math.sqrt(b)==3:
        listsr3.append(b)
        listsr3fr.append(c)
    if math.sqrt(b)==4:
        listsr4.append(b)
        listsr4fr.append(c)
    if math.sqrt(b)%2==0:
        listsrd2.append(b)
        listsrd2fr.append(c)        
    
zlist2 = zip(list2,list2fr)
zlist3 = zip(list3,list3fr)
zlist4 = zip(list4,list4fr)
zlist5 = zip(list5,list5fr)
zlist6 = zip(list6,list6fr)
zlist7 = zip(list7,list7fr)
zlist8 = zip(list8,list8fr)
zlist9 = zip(list9,list9fr)
zlist10 = zip(list10,list10fr)
zlistsr2 = zip(listsr2,listsr2fr)
zlistsr3 = zip(listsr3,listsr3fr)
zlistsr4 = zip(listsr4,listsr4fr)
zlistsrd2 = zip(listsrd2, listsrd2fr)

print("Fractions:")
print(listfr)
print("")
print("Divisible by 2")
print(list(zlist2))
print("")
print("Divisible by 3")
print(list(zlist3))
print("")
#print("Divisible by 3, remainder 1")
#print(list31)
print("")
print("Divisible by 4")
print(list(zlist4))
print("")
print("Divisible by 5")
print(list(zlist5))
print("")
print("Divisible by 6")
print(list(zlist6))
print("")
print("Divisible by 7")
print(list(zlist7))
print("")
print("Divisible by 8")
print(list(zlist8))
print("")
print("Divisible by 9")
print(list(zlist9))
print("")
print("Divisible by 10")
print(list(zlist10))
print("")
print("Squareroot is 2")
print(list(zlistsr2))
print("")
print("Squareroot is 3")
print(list(zlistsr3))
print("")
print("Squareroot is 4")
print(list(zlistsr4))

"""
w= int(input('Width of multiplication table: '))
h= int(input('Height of multiplication table: '))
for x in range(1,h+1):
    for y in range(1,w+1):
       print("{0: >3} ".format(x/y), end="")
    print()

import math
lista = []
listb = []
listc = []
listd = []
a = 0
b = 0
d = int(input("Largest Denominator?"))
for x in range(0,d):
    print(x)
    a += 1
    b = 1
    c = a/b
    if x == 0:
        lista.append(c)
        for y in range(0,d-1):
            a = a
            b += 1
            c = a/b
            lista.append(c)
    if x == 1:
        listb.append(c)
        for x in range(0,d-1):
            a = a
            b += 1
            c = a/b
            listb.append(c)
    if x == 2:
        listc.append(c)
        for x in range(0,d-1):
            a = a
            b += 1
            c = a/b
            listc.append(c)
    if x == 3:
        listd.append(c)
        for x in range(0,d-1):
            a = a
            b += 1
            c = a/b
            listd.append(c)        
print(lista)
print(listb)
print(listc)
print(listd)



n = int(input("I will estimate pi. How many terms should I use? "))
decimals = int(input("How many decimal places should I use in the result? "))
pi = float(4*(sum([((-1.0)**k)/(2*k+1) for k in range(0,n)])))
print("The approximate value of pi is {0}".format(round(pi, decimals)))
"""
