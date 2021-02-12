#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:27:02 2021

@author: alef
"""

def fib(n):
    """Fibonacci:
        fib(n) = fib(n-1) + fib(n-2) se n > 1
        fib(n) = 1 se n <= 1
    """
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1
# mostrar fibonacci de 1 a 5
for i in [1,2,3,4,5]:
    print(i,' => ',fib(i))
    
def fib_nr(n):
    """Fibonacci:
        fib(n) = fib(n-1) + fib(n-2) se n > 1
        fib(n) = 1 se n <= 1
    """
    
    #
    seq = [1,1]
    
    #calculando os outros
    for i in range(2, n + 1):
        seq.append(seq[i-1] + seq[i-2])
    
    return seq[n]

for i in [1,2,3,4,5]:
    print(i,'=>', fib(i))