#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:28:46 2021

@author: alef
"""

""" Exercicio 01

1. Implementar duas funções:
    - Uma que converta temperatura em graus Celsius para Fahrenheit
    - Outra que covnerta temperatura em graus Fahrenheit para Celsius
    
    Formula:
    F = 9/2 . C + 32
    C = (f-32)/1.8

"""

def celsius_for_fahrenheit(C):
    return (9/5) * C + 32 

def fahrenheit_for_celsius(F):
    return (F - 32) / 1.8


print(celsius_for_fahrenheit(0))
print(fahrenheit_for_celsius(32))

print(celsius_for_fahrenheit(55))
print(fahrenheit_for_celsius(131))