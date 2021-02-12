#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 22:47:12 2021

@author: alef
"""
# importa o modulo string
import string

# o alfabeto 
a = string.ascii_letters

# rodando o alfabeto um caractere para a esquerda
b = a[1:] + a[0]

# cria uma tabela de tradução enter caracteres de duas strings que
# recebe como parâmetro. os caracteres ausentes nas tableas serão copiados
# para a saída
tab = str.maketrans(a,b)

msg = '''esse texto será traduzido..
vai ficar bem estranho.'''

# função translate usa a tabela de tradução 
# criada pela maketrans para traduzir uma string
print(str.translate(msg, tab))

# cria uma string template
st = string.Template('$aviso aconteceu em $quando')

# preenche o modelo com um dicionário
s = st.substitute({'aviso' : 'Falta de eletricidade',
                   'quando': '01 de abril de 2002'})

print(s)