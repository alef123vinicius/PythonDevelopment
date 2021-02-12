#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:25:28 2021

@author: alef
"""

# Exempo de como receber todos parâmetros
# *args - argumentos sem nome (lista)
# ** kargs - argumentos com nome (dicionário)

def func(*args, **kargs):
    print(args)
    print(kargs)
    
func('peso',10,unidade='k')