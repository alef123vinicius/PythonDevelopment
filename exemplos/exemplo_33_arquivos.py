#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:38:33 2021

@author: alef
"""

import sys

# Criando um ubjeto do tipo file
temp = open('temp.txt', 'w')

# Escrevendo no arquivo 
for i in range(100):
    temp.write('%03d\n' % i)
    
# fechando 
temp.close()

temp = open('temp.txt')

# escrevendo no terminal
for x in temp:
    # Escrever em sys.stdout envia
    # o texto para a saída padrão
    sys.stdout.write(x)

temp.close()