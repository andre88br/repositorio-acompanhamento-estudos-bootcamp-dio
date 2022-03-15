import json
import urllib.error
from urllib.request import urlopen


url = "https://ipinfo.io/json"

try:
    resposta = urlopen(url)
    dados = json.load(resposta)

    ip = dados['ip']
    org = dados['org'].split(' ')[1] + " " + dados['org'].split(' ')[2]
    cid = dados['city']
    pais = dados['country']
    regiao = dados['region']

    print('IP: {}\n'
          'Operadora: {}\n'
          'Cidade: {}\n'
          'Estado: {}\n'
          'País: {}'.format(ip, org, cid, pais, regiao))

except urllib.error.HTTPError as ex:
    print(ex)





