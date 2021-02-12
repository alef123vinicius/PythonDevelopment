#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:51:20 2021

@author: alef


6. Crie uma função que:
- Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão
igual) e um booleano (reverso, falso por padrão).
- Retorne dados ordenados pelo item indicado pela chave e em ordem
decrescente se reverso for verdadeiro.
"""
def modify_data(lista, chave=0, is_reverse=False):
        return sorted(lista, key=lambda student: student[chave], reverse=is_reverse)

clientes = [(0,1),(2,7),(3,6),(4,4),(5,2)]

print(modify_data(clientes))
print(modify_data(clientes, is_reverse=True))
print(modify_data(clientes, chave=1))
print(modify_data(clientes, chave=1, is_reverse=True))


