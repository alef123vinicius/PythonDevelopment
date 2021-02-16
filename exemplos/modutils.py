#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:35:26 2021

@author: alef

modutils => rotinas utilitarias para módulos
"""

import os.path
import sys
import glob

def find(txt):
    """ encontra módulo que tem o nome
    contendo o parâmetro
    """
    
    resp = []
    
    for path in sys.path:
        mods = glob.glob('%s/*.py' % path)
        
        for mod in mods:
            if txt in os.path.basename(mod):
                resp.append(mod)
    
    return resp



