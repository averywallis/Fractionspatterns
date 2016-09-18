"""
calculatepi.py
Author: Avery Wallis

This was an experiment for Math Modeling and Fractions

"""
import math
lista = []
listb = []
a = 0
b = 0
for x in range(0,2):
    a += 1
    b = 1
    c = a/b
    if x == 0:
        lista.append(c)
        for y in range(0,2):
            a = a
            b += 1
            c = a/b
            lista.append(c)
    if x == 1:
        listb.append(c)
        for x in range(0,1):
            a = a
            b += 1
            c = a/b
            listb.append(c)
print(lista)
print(listb)

d = lista[1]

print(d)



"""
n = int(input("I will estimate pi. How many terms should I use? "))
decimals = int(input("How many decimal places should I use in the result? "))
pi = float(4*(sum([((-1.0)**k)/(2*k+1) for k in range(0,n)])))
print("The approximate value of pi is {0}".format(round(pi, decimals)))
"""
