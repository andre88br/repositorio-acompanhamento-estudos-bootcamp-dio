
lista = [12, 10, 7, 5, 11]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animais[0] = 'macaco'
print(lista_animais)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animais))

tupla_animais = tuple(lista_animais)
print(type(tupla_animais))
print(tupla_animais)

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)


# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# lista.reverse()
# lista_animais.reverse()
# print(lista_animais)
# print(lista)


# print(lista_animais[1])

# if 'lobo' in lista_animais:
#     print('Existe lobo na lista!')
# else:
#     print('Não existe lobo na lista! Será incluído!')
#     lista_animais.append('lobo')
#     print(lista_animais)
#
# lista_animais.pop()
# print(lista_animais)

