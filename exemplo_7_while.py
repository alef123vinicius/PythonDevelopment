#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:15:32 2021

@author: alef
"""

"""
função range: range(m,n,p) onde m é o início até n-1, em passos de p
       while: estrutura condicional parecida com o for
      
sintaxe

while <condição>:
    <bloco de codigo>
    continue
    break
else:
    <bloco de código>

indicado quando não há como determinar quantas iterações vão ocorrer e não há uma sequência a seguir
"""

# soma de 0 a 99

s = 0
x = 1

while x < 100:
    s = s + x
    x = x + 1
print(x)
