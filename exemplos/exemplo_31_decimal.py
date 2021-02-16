#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:25:42 2021

@author: alef

O módulo decimal define operações com números reais com precisão fixa.
Com este módulo é possível reduzir a introdução de erros de
arredondamento originados da atirmética de ponto flutuante.

"""

from decimal import Decimal

t = 5.
for i in range(50):
    t = t - 0.1
    
print('Float:',t)

t = Decimal('5.')
for i in range(50):
    t = t - Decimal('0.1')
    #print('t:',t, Decimal('0.1'))

print('Decimal:',t)
