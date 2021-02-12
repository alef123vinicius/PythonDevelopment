#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:39:27 2021

@author: alef
"""

"""
Implementar uma função que retorne verdadeiro se o número for primo
falso caso o contrário. Testar de 1 a 100

"""

def primo(num):
    soma = 0
    for i in range(1, num+1):
        # print('i = >',i)
        if(num % i == 0):
            soma = soma + 1
    #print('soma:',soma)
    return False if (soma > 2 or soma == 1)  else True


for i in range(1,100):
    print('num:',i,' é primo? => ', primo(i))