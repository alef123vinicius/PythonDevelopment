#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 15:09:18 2021

@author: alef
"""

"""
For: aceita sequencias estáticas e iteradores. 
Iteradores acessam elementos de forma sequencial
Com o for a referência aponta para cada elemento a cada iteração.

o break pode ser usado para interromper o laço 
o continue passa direto para a proxima iteração

sintaxe

for <referência> in <sequencia>:
    <bloco de código>
    continue
    break
else:
    # este codigo é executado ao final do laço, a não ser que o laço tenha 
    # sido interrompido por break
    <bloco de código>
"""

# soma de 0 a 99 
s = 0
for x in range(1,100):
    s = s + x
print(s)