#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:16:54 2021

@author: alef

o módulo math define funções logarítmicas, de exponenciação, trigonométricas, 
hiperbólicas e conversões, entre outras. Já o cmath, implenenta funções similares,
porém feitas para processar números complexos.

"""

# Módulo para matemática
import math

# Módulo para matemática de números complexos
import cmath

# Complexos
for cpx in [3j,1.5 + 1j, -2 - 2j]:
    plr = cmath.polar(cpx)
    print('Complexo:',cpx)
    print('Forma polar:',plr,'(em radianos)')
    print('Amplitude:',abs(cpx))
    print('Ângulo:',math.degrees(plr[1]),'(graus)')