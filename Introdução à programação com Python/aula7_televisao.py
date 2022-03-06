
class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 3

    def botao_power(self):
        if self.ligada == False:
            self.ligada = True