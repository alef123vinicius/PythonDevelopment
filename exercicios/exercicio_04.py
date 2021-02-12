#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:16:53 2021

@author: alef


4. Implementar uma função que receba um dicionário e retorne a soma, a
média e a variação dos valores.
"""

import statistics

def analise_dados(saldo_filiais):
    total = 0
    count = 0
    data = []
    for filial,valores in saldo_filiais.items():
        print(filial,' ==> ', valores)
        count += len(valores)
        data.extend(valores)
        for valor in valores:
            total += valor
    media = float(total)/float(count) if count > 0 else 0
    variance = statistics.pvariance(data, mu=media)
    return total, media,variance

filiais = {'filial1':[100.0, 200.0, 500.0],
           'filial2':[250.0, 00.50, 300.0],
           'filial3':[700.0, 900.0, 100.0]}

result = analise_dados(filiais)

print('    Soma: ', result[0])
print('   Média: ', result[1])
print('variação: ', result[2])