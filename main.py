#!/usr/bin/python3
# -*- coding: utf-8 -*-

""" 
Biblioteca qrcode é necessária nesse projeto.
pip install qrcode[pil], ou
pip3 install qrcode[pil]

Sugiro fortemente utilisar um ambiente virtual caso queira apenas testar.
"""
import qrcode
import json

# Esse texto pode receber um set do sistema para gerar uma imágem nova
codigo_produto = 'LAT335699'
descricao = 'LEITE CONDENCADO'
lote = '2021-AX325-07'
data_fabricacao = '12/07/2021'
data_vencimento = '12/07/2023'

conteudo = {
    'CodProd': codigo_produto,
    'Descricao': descricao,
    'Lote': lote,
    'DataFabr': data_fabricacao,
    'DataVenc': data_vencimento
}

conteudo_convertido = json.dumps(conteudo)

""" arquivo = open('dados_produto.json', 'w')
arquivo.write(conteudo_convertido)
arquivo.close() """

img = qrcode.make(conteudo_convertido)

type(img)  # qrcode.image.pil.PilImage
img.save("some_file.png")

# A saida será uma imágem png cujo conteúdo será:
# {Lote: "2021-AX325-07", DataFabr: "12/07/2021", DataVenc: "12/07/2023"}
# Esse texto pode ser usado tranquinamente por um interpretador qualquer
# para inplementação no sistema de ERP para fazer o controle do produto.
