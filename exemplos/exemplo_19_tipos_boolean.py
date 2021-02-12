#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 15:19:12 2021

@author: alef
"""

"""
boolean é uma especialização do tipo inteiro. veraddeiro é True e igual a 1,
enquanto o falso é chamado de False e é ogual a zero.

São considerados falsos:
- False (falso)
- None (nulo)
- 0 (zero)
- ''(string vazia)
- [] (lista vazia)
- () (tupla vazia)
- {} (dicionario vazio)
- Outros estruturas de tamanho zero

Operadores Lógicos:
- and
- or 
- not
- in
- is: verdadeiro se receber duas referências do mesmo objeto
- in: verdadeiro se receber um item e uma lista e o item ocorrer uma ou mais vezes na lista

and: se a primeira expressão for verdadeiro o resultado será a segunda.
or : se a primeira expressão for falsa o resultado será a segunda expressão

"""

print(0 and 3) # mostra 0

print(2 and 3) # mostra 3

print(0 or 3) # mostra 3

print(not 0) # Mostra True

print(not 2) # Mostra False

print(2 in (2,3)) # Mostra True

# com o is sigeriu para utiliza o == ou !=
print((2,2) == (2,3)) # Mostra False


print(all([1,2,3,4])) # Mostra True

# retorna True se todos os itens foram verdadeiros
print(all([1,2,3,0])) # Mostra False

# retorna True se algum item for verdadeiro
print(any([1,2,3,0])) # Mostra True