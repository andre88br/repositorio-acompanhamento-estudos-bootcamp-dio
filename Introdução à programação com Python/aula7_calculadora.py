
class Calculadora:

    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subitracao(self):
        return self.valor_a - self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

a = float(input('N1: '))
b = float(input('N2: '))

calculadora = Calculadora(a, b)


print('{} + {} = {}'.format(calculadora.valor_a, calculadora.valor_b, calculadora.soma()))
print('{} - {} = {}'.format(calculadora.valor_a, calculadora.valor_b, calculadora.subitracao()))
print('{} * {} = {}'.format(calculadora.valor_a, calculadora.valor_b, calculadora.multiplicacao()))
print('{} / {} = {}'.format(calculadora.valor_a, calculadora.valor_b, calculadora.divisao()))
