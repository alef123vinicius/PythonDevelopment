#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:05:03 2021

@author: alef
"""

def rgb_html(r=0,g=0,b=0):
    """ Converte R, G, B r em #RRGGBB"""
    return '#%02x%02x%02x' % (r,g,b)

def html_rgb(color='#000000'):
    """Converte #RRGGBB em R, G, B"""
    
    if color.startswith('#'): color = color[1:]
                        
    r = int(color[:2] ,16)
    g = int(color[2:4],16)
    b = int(color[4:6],16)
    
    return r,g,b # uma sequencia
    
    
print(rgb_html(200,200,225))
print(rgb_html(b=200,g=200,r=255))
print(html_rgb('#c8c8ff'))