#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:25:40 2021

@author: alef
"""

"""
a partir da versão 2.6 existe o format alem do %

"""

musicos = [('Page', 'guitarrista', 'Led Zeppelin'),
           ('Fripp', 'guitarrista', 'King Crimson')]

# Paramentros identificados pela ordem
msg = '{0} é {1} do {2}'

for nome, funcao, banda in musicos:
    print(msg.format(nome,funcao,banda))
    
# Parâmetros identificados pelo nome
msg = '{saudacao}, são {hora:02d}:{minuto:02d}'

print(msg.format(saudacao='Bom dia', hora=7, minuto=30))

# Função builtin format() só pode ser usado apenas para um dado de cada vez
print('Pi=',format(3.14159, '.3e'))

s = 'python'

# pega o primeiro caractere
print(s[0])

# pega a substring py
print(s[:2])

# pega a substring thon
print(s[2:])

# pega a ultima letra
print(s[-1])

# pegou a palavra python invertida
print('python'[::-1])