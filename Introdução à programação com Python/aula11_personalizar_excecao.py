class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10 or x < 0:
            raise InputError('Nota deve estar entre 0 e 10!')
        break
    except ValueError:
        print('Valor inválido!')
    except InputError as ex:
        print(ex)
