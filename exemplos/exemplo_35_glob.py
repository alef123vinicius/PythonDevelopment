#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:52:22 2021

@author: alef
"""

import os.path
import glob

# Mostra uma lista de nomes de arquivos
# e seus respectivos tamanhos
for arq in sorted(glob.glob('*.py')):
    print(arq, os.path.getsize(arq))