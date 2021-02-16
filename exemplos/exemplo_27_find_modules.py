#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:40:03 2021

@author: alef
"""

from os.path import getsize, getmtime
from time import localtime, asctime

import modutils

mods = modutils.find('xml')

for mod in mods:
    tm = asctime(localtime(getmtime(mod)))
    kb = getsize(mod) / 1024
    print('%s: (%d kbytes, %s)' % (mod,kb,tm))
    print('test')
    print(mod,kb,tm)