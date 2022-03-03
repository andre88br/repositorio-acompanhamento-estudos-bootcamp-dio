a = int(input('Insira um número: '))
b = int(input('Insira outro número: '))

adicao = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = 'Soma: {a} \n' \
            'Subtração: {s}\n' \
            'Divisão: {d}\n' \
            'Multipricação: {m}\n' \
            'Resto: {r}'\
            .format(a=adicao, s=subtracao, m=multiplicacao, d=divisao, r=resto)

print(resultado)
