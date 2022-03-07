import requests


def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    dados_cep = response.json()
    return '{} - Bairro:{}\n' \
           'CEP:{} - {}/{}' \
           .format(dados_cep['logradouro'], dados_cep['bairro'], dados_cep['cep'], dados_cep['localidade'], dados_cep['uf'])


cep1 = int(input('Informe o cep: '))

print(retorna_dados_cep(cep1))
