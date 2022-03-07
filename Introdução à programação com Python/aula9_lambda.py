
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'divisao': lambda a, b: a / b,
    'multiplicacao': lambda a, b: a * b
}

num1, num2 = 0, 0
operacao = 0

while num1 == 0 or type(num1) is not int:
    try:
        num1 = int(input('N1: '))
    except TypeError:
        print('N1 deve ser um número inteiro!')
    except ValueError:
        print('N1 deve ser um número inteiro!')


while num2 == 0 or type(num2) is not int:
    try:
        num2 = int(input('N2: '))
    except TypeError:
        print('N2 deve ser um número inteiro!')
    except ValueError:
        print('N2 deve ser um número inteiro!')


while operacao < 1 or operacao > 4 or type(operacao) is not int:
    try:
        operacao = int(input('1 - Soma\n'
                             '2 - Subtração\n'
                             '3 - Divisão\n'
                             '4 - Multiplicação\n'
                             'Escolha uma das opções: '))
        if operacao == 1:
            print('{} + {} = {}'.format(num1, num2, calculadora['soma'](num1, num2)))
        elif operacao == 2:
            print('{} + {} = {}'.format(num1, num2, calculadora['subtracao'](num1, num2)))
        elif operacao == 3:
            print('{} / {} = {}'.format(num1, num2, calculadora['divisao'](num1, num2)))
        elif operacao == 4:
            print('{} * {} = {}'.format(num1, num2, calculadora['multiplicacao'](num1, num2)))
        else:
            print('Opção inválida! Escolha outra opção!')
    except TypeError:
        print('Opção inválida! Escolha outra opção!')
    except ValueError:
        print('Opção inválida! Escolha outra opção!')
