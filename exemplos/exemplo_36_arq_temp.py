#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 00:55:11 2021

@author: alef

No presente momento a biblioteca os indicada no livro não apresenta mais
a função tmpfile, a documentação sugere utilizar a biblioteca temfile
como o exemplo abaixo para criar arquivos temporarios.
"""

import tempfile

texto = 'Teste'

# cria um arquivo temporário
temp = tempfile.TemporaryFile()

# Escreve no arquivo temporário
temp.write('Teste')

# Volta para o inicio do arquivo
temp.seek(0)

# mostra o conteúdo do arquivo
print(temp.read())

# fecha o arquivo
temp.close()