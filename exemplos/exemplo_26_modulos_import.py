#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:17:27 2021

@author: alef
"""
# importação absoluta
import os

# importação relativa
# from os import name

# para importar tudo que está definido no módulo
# from os import *

# Arquivo criado no mesmo diretório 
import calc

i = [23, 54, 31, 77, 12, 34]

print(os.name)

print(calc.media(i))


"""
o módulo principal de um programa tem variável __name__ igual à "__main__"

if __name__ == "__main__":
    # aqui o código será executado
    # se este for o módulo principal
    # e não quando ele for improtado por outro programa


"""