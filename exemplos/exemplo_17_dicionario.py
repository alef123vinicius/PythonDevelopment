#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 14:17:57 2021

@author: alef
"""

# progs e seus albuns
progs = {'Yes':['Close to the Edge', 'Fragile'],
         'Genesis':['Foxtrot', 'The Nursey Crime'],
         'ELP':['Brain Salad Surgery']}

# mais progs
progs['King Crimson'] = ['Red', 'Discipline']

# items() retorna uma lista de tuplas com a chave e o valor
for prog, albuns in progs.items():
    print(prog,'=>',albuns)
    
# Se tiver 'ELP', deleta
if(progs.get('ELP')):
    del progs['ELP']
    
