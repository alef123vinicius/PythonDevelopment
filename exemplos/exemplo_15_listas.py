#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 12:34:36 2021

@author: alef
"""

"""
lista são coleções heterogêneas de objetos, que podem ser de qualquer tipo, 
inclusive outras lista. 
Listas são mutáveis, listas podem ser alteradas e quebradas.

sintaxe = [a,b,...,z]

Operações comuns

"""

# Uma nova lista: Brit dos anos 70
progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']

# Varrendo a lista inteira
for prog in progs:
    print(prog)
    
# Trocando o último elemento
progs[-1] = 'King Crimson'

# Incluindo
progs.append('Camel')

# Removendo
progs.remove('Pink Floyd')

# Ordena a lista
progs.sort()

# inverte a lista
progs.reverse()

# imprime numerado
# enumerate retorna uma tupla de dois elementos o index e o item
for i,prog in enumerate(progs):
    print(i + 1, '=>', prog)
    
# Imprime do segundo item em diante
print(progs[1:])

lista = ['A', 'B', 'C']

print('lista:', lista)

# A lista vazia é avaliada como falsa
while lista:
    
    # Em filas, o primeiro item é o primeiro a sair
    # pop(0) remove e retorna o primeiro item
    print('Saiu', lista.pop(0),', faltam ', len(lista))

# Mais itens na lista
lista += ['D', 'E', 'F']

print('lista: ', lista)

while lista:
    
    # Em pilhas, o primeiro item é o último a sair
    # pop() remove e retorna o último item
    print('saiu: ', lista.pop(), ',faltam ', len(lista))