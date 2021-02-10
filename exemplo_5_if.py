#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:57:33 2021

@author: alef
"""

"""
Estrutura condicional 

       Condição: sentença que possa ser avaliada como verdadeira ou falsa
bloco de código: sequencias de linhas de comando
    elif e else: são opcionais e por sintaxe pode-se ter varios 
                 elif para um if mais somente um else
     Parênteses: necessarios para evitar ambiguidades

if (<condição>):
    <bloco de código>
elif (<condição>):
    <bloco de código>
elif (<condição>):
    <bloco de código>
else:
    <bloco de código>
"""
# input: comando utilizado para receber uma entrada do usuário na tela
#   int: comando para formatar o valor recebido pelo input para inteiro

temp = int(input('Entre com a temperatura: '))

if temp < 0:
    print('Congelando...')
elif 0 <= temp <=20:
    print('Frio')
elif 21 <= temp <= 25:
    print('Normal')
elif 26 <= temp <= 35:
    print('Quente')
else:
    print('Muito quente')
