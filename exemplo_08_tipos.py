#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:25:21 2021

@author: alef

Tipos 

- Numeros(inteiros, reais, complexos)
- Texto

- Lista
- Tupla
- Dicionario

- o tipo mutável permite alterar valores nas variáveis
- o tipo imutável não permite alterar o conteúdo da variável

builtins: estão sempre disponíveis em tempo de execução, sem a necessidade
de importar nenhuma biblioteca

- Inteiro (int): i = 1
- Real de ponto flutuante (float): f = 3.14
- Complexo (complex): c = 3 + 4j

"""

# convertendo de real para inteiro
print('int(3.14) = ', int(3.14))

# convertendo de inteiro para real
print('float(5) = ', float(5))

# calculo entre inteiro e real e resulta em real
print('5.0 / 2 + 3 = ', 5.0 / 2 + 3)

#inteiros em outra base
print("int('20', 8) = ", int('20', 8))

print("int('20', 16) = ", int('20', 16))

# operações com numeros complexos

c = 3 + 4j

print("c=",c)
print("Parte real:", c.real)
print("Parte imaginária: ", c.imag)
print("Conjugado", c.conjugate())