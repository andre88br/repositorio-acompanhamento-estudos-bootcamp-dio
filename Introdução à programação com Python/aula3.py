
a = int(input('Nota primeiro bimestre: '))
if a > 10:
    a = int(input('A nota deve estar entre 0 e 10. Nota primeiro bimestre: '))

b = int(input('Nota segundo bimestre: '))
if b > 10:
    b = int(input('A nota deve estar entre 0 e 10. Nota segundo bimestre: '))

c = int(input('Nota terceiro bimestre: '))
if c > 10:
    c = int(input('A nota deve estar entre 0 e 10. Nota terceiro bimestre: '))

d = int(input('Nota quarto bimestre: '))
if d > 10:
    d = int(input('A nota deve estar entre 0 e 10. Nota quarto bimestre: '))

media = (a + b + c + d) / 4

print('A média do aluno no ano foi {}'.format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#         print('A média do aluno no ano foi {}'.format(media))
# else:
#     print('Foi informada alguma nota errada"')


# a = int(input('Entre com um valor: '))
# b = int(input('Entre com outro valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um número par!')
# else:
#     print('Não foi digitado um número par!')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}.'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}.'.format(b))
# else:
#     print('O maior número é {}.'.format(c))
# print('Final do programa!')