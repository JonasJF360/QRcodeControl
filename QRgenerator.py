# -*- coding: utf-8 -*-

""" 
Biblioteca qrcode é necessária nesse projeto.
pip install qrcode[pil], ou
pip3 install qrcode[pil]

Sugiro fortemente utilisar um ambiente virtual caso queira apenas testar.
"""
import qrcode
import json
from datetime import datetime


dataHora = datetime.now().strftime('%d_%m_%Y-%H_%M_%S')

# Esse texto pode receber um set do sistema para gerar uma imágem nova
codigo_produto = 'LAT335699'
descricao = 'PRODUTO EXEMPLO 50ML'
lote = '2021-AX325-07'
data_fabricacao = '19/01/2022'
data_vencimento = '15/08/2023'

conteudo = {
    'CodProd': codigo_produto,
    'Descricao': descricao,
    'Lote': lote,
    'DataFabr': data_fabricacao,
    'DataVenc': data_vencimento
}

# Criação de um arquivo json
conteudo_convertido = json.dumps(conteudo)
arquivo = open('statics/dados_produto.json', 'w')
arquivo.write(conteudo_convertido)
arquivo.close()

# Criação do QRcode
img = qrcode.make(conteudo_convertido)

type(img)  # qrcode.image.pil.PilImage
img.save(f"statics/QRfile_{dataHora}.png")

arquivo = open('statics/UltimoQRfile.txt', 'w')
arquivo.write(f"statics/QRfile_{dataHora}.png")
arquivo.close()
