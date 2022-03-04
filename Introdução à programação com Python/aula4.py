
a = float(input('Nota primeiro bimestre: '))
while a > 10:
    a = float(input('A nota deve estar entre 0 e 10. Nota primeiro bimestre: '))

b = float(input('Nota segundo bimestre: '))
while b > 10:
    b = float(input('A nota deve estar entre 0 e 10. Nota segundo bimestre: '))

c = int(input('Nota terceiro bimestre: '))
while c > 10:
    c = float(input('A nota deve estar entre 0 e 10. Nota terceiro bimestre: '))

d = float(input('Nota quarto bimestre: '))
while d > 10:
    d = float(input('A nota deve estar entre 0 e 10. Nota quarto bimestre: '))

media = (a + b + c + d) / 4

print('A média do aluno no ano foi {:.2f}'.format(media))


# a = int(input('Informe um número: '))
#
# for num in range(a+1):
#     cont = 0
#     for x in range(1, num+1):
#         resto = num % x
#         if resto == 0:
#             cont += 1
#     if cont == 2:
#         print('O número {} é primo!'.format(num))


# a = int(input('Entre com um número: '))
# cont = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         cont += 1
# if cont < 2:
#     print('O número {} é primo!'.format(a))
# else:
#     print('O número {} não é primo!'.format(a))
