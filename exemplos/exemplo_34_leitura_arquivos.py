#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:42:47 2021

@author: alef
"""

import sys
import os.path

# input() retorna a string digitada
fn = input('Nome do arquivo: ').strip()

if not os.path.exists(fn):
    print('Tente outra vez...')
    sys.exit()
    
# Numerando as linhas
for i,s in enumerate(open(fn)):
    print(i + 1, s)
    
print('Com o método readlines')

print(open('temp.txt').readlines())

# Retorna o componente final de um caminho
print(os.path.basename('/home/alef/Área de Trabalho/cursos_e_livros/estudo_python/python_para_desenvolvedores/PythonDevelopment/exemplos/temp.txt'))

# Retorna um caminho sem o componente final
print(os.path.dirname('/home/alef/Área de Trabalho/cursos_e_livros/estudo_python/python_para_desenvolvedores/PythonDevelopment/exemplos/temp.txt'))

# Retorna True se um caminho existe ou False em caso contrário
print(os.path.exists('/home/alef/Área de Trabalho/cursos_e_livros/estudo_python/python_para_desenvolvedores/PythonDevelopment/exemplos/temp.txt'))

# Retorna o tamanho do arquivo em bytes
print(os.path.getsize('/home/alef/Área de Trabalho/cursos_e_livros/estudo_python/python_para_desenvolvedores/PythonDevelopment/exemplos/temp.txt'))