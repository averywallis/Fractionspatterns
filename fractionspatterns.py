"""
calculatepi.py
Author: Avery Wallis

This was an experiment for Math Modeling and Fractions

"""
import math
lista = []
listb = []
listc = []
listd = []
a = 0
b = 0
d = int(input("Largest Denominator?"))
for x in range(0,d):
    a = 1
    b += 1
    c = a/b
    lista.append(c)
    if lista[x]%2==0:
        listb.append(c)
print(lista)
print(listb)



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
