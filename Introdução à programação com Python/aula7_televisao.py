
class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 3

    def botao_power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def sobe_canal(self):
        if self.ligada:
            self.canal += 1
        else:
            print('A TV está desligada')

    def desce_canal(self):
        if self.ligada:
            self.canal -= 1
        else:
            print('A TV está desligada')

    def mostra_canal(self):
        if self.ligada:
            return self.canal
        else:
            return 'A televisão está desligada'


televisao = Televisao()

televisao.botao_power()

print('A televisão está ligada? {}'.format(televisao.ligada))
print('Canal: {}'.format(televisao.mostra_canal()))
