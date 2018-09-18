# -*- coding: utf-8 -*-
from random import randint
from math import sqrt
def milpri(n):
    if type(n) != int or n < 2: return False
    if n == 2: return True
    if n & 1 == 0: return False
    if n < 5000:
        for i in range(3,int(sqrt(n))+1,2):
            if n%i == 0: return False
        return True
    d = (n - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in range(100):
        a = randint(1,n-1)
        t = d
        y = pow(a, t, n)
        while t !=n - 1 and y != 1 and y != n -1:
            y = (y * y) % n
            t <<= 1
        if y != n - 1 and t & 1 == 0: return False
    return True
