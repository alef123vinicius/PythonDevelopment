#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 01:04:56 2021

@author: alef

Gravando texto em um arquivo compactado
"""

import zipfile

texto = """
***************************************
Esse é o texto que será compactado e...
... guardado dentro de um arquivo zip.
***************************************
"""

# cria um zip novo
zip_file = zipfile.ZipFile('arq.zip','w', zipfile.ZIP_DEFLATED)

# Escreve uma string no zip como se fosse um arquivo
zip_file.writestr('text.txt', texto)

# fecha o zip
zip_file.close()


# leitura do arquivo

# Abre o arquivo zip para leitura
zip_file = zipfile.ZipFile('arq.zip')

# Pega a lista dos arquivos compactados
arqs = zip_file.namelist()

for arq in arqs:
    # Mostra o nome do arquivo
    print('Arquivo:', arq)
    
    # Pegando as informações do arquivo
    zipinfo = zip_file.getinfo(arq)
    print('Tamanho original: ', zipinfo.file_size)
    print('Tamanho comprimido: ',zipinfo.compress_size)
    
    # Mostra o conteúdo do arquivo
    print('%s' % zip_file.read(arq).decode())