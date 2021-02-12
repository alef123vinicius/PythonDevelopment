#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:57:18 2021

@author: alef
"""

"""
Matriz esparça como dicionario

Matriz esparça é uma estrutura que só armazena os valores 
que existem na matriz

"""

dim = 6,12
mat = {}

mat[3,7] = 3
mat[4,6] = 5
mat[6,3] = 7
mat[5,4] = 6
mat[2,9] = 4
mat[1,0] = 9

for lin in range(dim[0]):
    for col in range(dim[1]):
        print(mat.get((lin, col),0))
    print('\n')
    
# Matriz em forma de string
matriz = '''0 0 0 0 0 0 0 0 0 0 0 0
            9 0 0 0 0 0 0 0 0 0 0 0
            0 0 0 0 0 0 0 0 0 4 0 0
            0 0 0 0 0 0 0 3 0 0 0 0
            0 0 0 0 0 0 5 0 0 0 0 0    
            0 0 0 0 6 0 0 0 0 0 0 0
         '''
         
mat = {}

# quebra a matriz em linhas 
for lin, linha in enumerate(matriz.splitlines()):
    
    # Quebra a linha em colunas
    for col, coluna in enumerate(linha.split()):
        
        coluna = int(coluna)
        # coloca a coluna no resultad, se for diferente de zro
        if(coluna):
            mat[lin,col] = coluna

print(mat)

print('Tamanho da matriz completa: ',((lin + 1)*(col + 1)))  
print('Tamanho da matriz esparsa:', len(mat))