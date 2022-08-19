
from datetime import datetime

class Pessoa2:
    
    # criando uma variavel da classe( porém para usar essa variável, você precisa usar o 'self')
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    # método especial(função especial)
    def __init__(self, nome, idade, comendo = False, falando = False):
        # os valores do parametro vao pro self.parametro, serve para cada variavel ter o seu valor especifico
        # tu pode usar qualquer uma dessas variavels em outros métodos dessa classe
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def get_ano_nasc(self):
        return self.ano_atual - self.idade