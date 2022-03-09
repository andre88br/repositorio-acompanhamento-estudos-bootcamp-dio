import random, string

tamanho = int(input('Digite o tamanho de senha que você deseja: '))

chars = string.ascii_letters + string.digits + 'ç!@#$%&*(),.;:/?'

rnd = random.SystemRandom()

senha = ''

for i in range(tamanho):
    caracter_atual = rnd.choice(chars)
    if i == 0:
        senha += caracter_atual
    elif caracter_atual in senha:
        while caracter_atual in senha:
            caracter_atual = rnd.choice(chars)
        senha += caracter_atual
    else:
        senha += caracter_atual

print(senha)
