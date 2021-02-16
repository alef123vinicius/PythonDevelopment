#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:22:38 2021

@author: alef
"""

import csv 

# Dados 
dt = (('temperatura', 15.0, 'C', '10:40', '2006-12-31'),
      ('peso', 42.5, 'kg', '10:45', '2006-12-31'))

# a rotina de escrita recebe um objeto do tipo file
out = csv.writer(open('dt.csv', 'w'))

# escrevendo as tuplas no arquivo
out.writerows(dt)

# A rotina de leitura recebe um objeto arquivo
dt_read = csv.reader(open('dt.csv'))

# Para cada registro do arquivo, imprima
for reg in dt:
    print(reg)