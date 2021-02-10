#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:54:31 2021

@author: alef
"""

"""
Função puramente educacional e não esta atualmente nas versões > 3.x
Essa função permite a mutabilidade de strings
"""

import UserString

s = UserString.MutableString('python')

print(s)

s[0] = 'P'

print(s)