#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:05:53 2021

@author: alef
"""

# String unicode
u = u'Hüsker Dü'

print(u, type(u))

# Convertendo para str
s = u.encode('latin1')

print(s, '=>', type(s))

t = s.decode('latin1')

print(t, ' => ', type(t))
