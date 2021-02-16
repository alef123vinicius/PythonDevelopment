#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:21:10 2021

@author: alef

O módulo random traz funções para a geração de números aleatórios.

"""
import random
import string

# Escolha uma letra
print(random.choice(string.ascii_uppercase))

# Escolha um número de 1 a 10
print(random.randrange(1,11))

# Escolha um float no intervalo de 0 a 1
print(random.random())
