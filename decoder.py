# Esse é apenas um exemplo simples de utilização para teste
# Leitura do conteúdo do QRcode estará em um formato apropriado
# para a converção com JSON.
import json

# É claro que o conteúdo seria capturado por um leirtor de QRcode
# e não importado de um JSON mas sua converção ajudaria muito.
arquivo = open('dados_produto.json', 'r')
conteudo = arquivo.read()
arquivo.close()

conteudo_dicionario = json.loads(conteudo)

print()
for x, y in conteudo_dicionario.items():
    print(x + ':', y)