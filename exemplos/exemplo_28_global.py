#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:55:49 2021

@author: alef
"""

def somalista(lista):
    """
    Soma listas de listas, recursivamente
    Coloca o resultado como global
    """
    
    global soma
    
    for item in lista:
        if type(item) is list:
            somalista(item)
        else:
            soma += item

soma = 0
somalista([[1,2],[3,4,5],6])

print(soma)