#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:39:51 2021

@author: alef


5. Escreva uma função que:
- Receba uma frase como parâmetro.
- Retorne uma nova frase com cada palavra com as letras invertidas.
"""

def inverte_palavras(frase):
    test = frase.split(' ')
    result = ''
    for p in test:
        result += p[::-1] +' '
    
    return result

frase = 'batatinha roxa no coração dos trouxas'
print(' original: ', frase)
print('invertido: ', inverte_palavras(frase))