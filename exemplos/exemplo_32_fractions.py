#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:32:04 2021

@author: alef

A função Fraction trata de números racionais.
Existe uma função chamada gcd() que calcula o maior divisor comum.
"""

from fractions import Fraction


f1 = Fraction('-2/3')
f2 = Fraction(3, 4)
f3 = Fraction('.25')

print('Fraction(\'-2/3\') = ', f1)
print('Fraction(3, 4)   = ', f2)
print('Fraction(\'.25\')  = ', f3)

print(f1,'+',f2,'=',f1+f2)
print(f2,'+',f3,'=',f2+f3)
