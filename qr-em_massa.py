# projeto: baixar QRcode em massa
# Versão: 1
# Autor: FoxCrazy(Vitor de Souza)

import os 
urls = open('urls.txt','r')
numero = 1
for url in urls:
	comando = 'curl "https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={}" --output qr-code{}.png'.format(url.rstrip("\n"),numero)
	os.system(comando)
	numero += 1
urls.close()