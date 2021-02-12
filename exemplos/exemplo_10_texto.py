#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:20:09 2021

@author: alef
"""

"""
strings em python são buitins. são imutaveis sendo impossível de modificar.
para realizar operações em string é necessário criar uma nova string

String padrão: s= 'Led Zeppelin'
String unicode: u = u'Bjork'

A string padrão pode ser convertida para unicode com unicode()
Pode-se utilizar aspas simples ou duplas para iniciar uma string

 Símbolos usados na interpolação:
    %s: string.
    %d: inteiro.
    %o: octal.
    %x: hexacimal.
    %f: real.
    %e: real exponencial.
    %%: sinal de percentagem.

"""

s = 'Camel'

# Concatenação
print('The ' + s + ' run away!')

# Interpolação
print('Tamanho de %s => %d' % (s, len(s)))
# String tratada como sequência
for ch in s: print(ch)

# Strings são objetos
if s.startswith('C'): print(s.upper())

# o que acotnecerá? R: 3 * s é consistente com s + s + s
print(3 * s)

# Zeros a esquerda
print('Agora são %02d:%02d.'%(16, 30))

# Real (número após o ponto controla as casas decimais)
print('Percentagem: %.1f%%, Exponencial:%.2e'%(5.333, 0.00314))

# Octal e hexadecimal
print('Decimal %d, Octal: %o, Hexadecimal:%x'%(10,10,10))