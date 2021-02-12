#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:32:58 2021

@author: alef
"""

# sorted() ordena sequências 
# cmp()faz operações entre dois argumentos e retorna -1 se o primeiro
# elemento for maior, 0 se forem iguais e 1 se o ultimo elemento for maior

dados = [(4,3),(5,1),(7,2),(9,0)]

lista = [5,4,3,2,1]
print('Lista simple:', lista)
print('Ordenada: ', sorted(lista))

print('Lista:',dados)

# ordenando tuplas
print('Ordenada', sorted(dados, key=lambda student: student[1]))

print('Resultado:',eval('12./2 + 3.3'))