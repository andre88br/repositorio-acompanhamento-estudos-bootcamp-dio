
lista = [1, 10, 5, 90]
try:
    divisao = 10 / 0
    numero = lista[1]
    x = 0
except ZeroDivisionError:
    print('Não é possível realizar divisão por 0!')
except IndexError:
    print('A lista só possui as posições de 0 até {}!'.format(len(lista)-1))
except Exception as ex:
    print('Erro desconhecido! Erro: {}'.format(ex))
else:
    print('Sem erro!')
finally:
    print('Com erro ou sem!')