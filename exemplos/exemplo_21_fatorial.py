#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 17:26:43 2021

@author: alef
"""


#fatorial implementado de forma recursiva
def fatorial_r(num):
    if num <= 1:
        return 1
    else:
        return (num * fatorial_r(num - 1))

# fatorial sem recursão 1
def fatorial_nr(num):
    resp = list(range(num,1,-1)) if num > 1 else [1]
    soma = 1
    for i in resp:
        soma = soma * i
    return soma

def fatorial_nr2(n):
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n+1):
        j = j*i
    return j

for i in range(10):
    print(fatorial_r(i))
    print(fatorial_nr(i))
    print(fatorial_nr2(i))
