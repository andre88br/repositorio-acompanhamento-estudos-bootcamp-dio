class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'divisao': lambda a, b: a / b,
    'multiplicacao': lambda a, b: a * b
}

while True:
    try:
        num1 = int(input('N1: '))
        break
    except ValueError:
        print('N1 deve ser um número inteiro!')

while True:
    try:
        num2 = float(input('N2: '))
        break
    except ValueError:
        float('N2 deve ser um número inteiro!')

while True:
    try:
        operacao = int(input('1 - Soma\n'
                             '2 - Subtração\n'
                             '3 - Divisão\n'
                             '4 - Multiplicação\n'
                             'Escolha uma das opções: '))
        if operacao == 1:
            print('{} + {} = {:.2f}'.format(num1, num2, calculadora['soma'](num1, num2)))
        elif operacao == 2:
            print('{} + {} = {:.2f}'.format(num1, num2, calculadora['subtracao'](num1, num2)))
        elif operacao == 3:
            print('{} / {} = {:.2f}'.format(num1, num2, calculadora['divisao'](num1, num2)))
        elif operacao == 4:
            print('{} * {} = {:.2f}'.format(num1, num2, calculadora['multiplicacao'](num1, num2)))
        elif operacao < 1 or operacao > 4:
            raise InputError('Opção inválida! Escolha outra opção!')
        break
    except TypeError:
        print('Opção inválida! Escolha outra opção!')
    except ValueError:
        print('Opção inválida! Escolha outra opção!')
    except InputError as ex:
        print(ex)
    except Exception as ex:
        print('Erro desconhecido! Erro: {}'.format(ex))
