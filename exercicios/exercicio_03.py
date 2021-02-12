#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:50:06 2021

@author: alef
"""

"""
Implementar uma função que receba uma lista de listas de comprimentos
quaisquer e retorne uma lista de uma dimensão.

"""

def unique_lista(lista):
    unique = []
    for i in lista:
        if(type(i) == list or type(i) == tuple):
            sub_list = unique_lista(i)
            unique.extend(sub_list)
        else:
            unique.append(i)
    
    return unique


listas = [(1,2,(3,4),5),[6,7,8],(9,10),11.0]
print('Entrada:',listas)
print('  Saida:',unique_lista(listas))