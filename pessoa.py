

class Pessoa:
    #método especial(função especial)
    def __init__(self, nome, idade, comendo = False, falando = False):
        # os valores do parametro vao pro self.parametro, serve para cada variavel ter o seu valor especifico
        # tu pode usar qualquer uma dessas variavels em outros métodos dessa classe
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        # criando uma varial que só vale nessa funcao
        variavel = 'Valor'


    def outro_metodo(self):
        #tu pode usar uma variavel self em todos os metodos
        print(self.nome)

    def comer(self):
        print(f'{self.nome} está comendo')
        self.comendo = True
    
    # criando um metodo (função) que usa um self do metodo especial e um parametro da propria função
    def ingerindo(self,alimento):
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True
    
    # usando if no metodo
    def jantando(self,comida):
        if self.comendo == True:
            print(f'{self.nome} já está comendo')
            return

        print(f'{self.nome} está comendo {comida}.')
        self.comendo = True
    
    # criando um metodo para mudar a variavel self de "True" para "False"
    def parar_jantar(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comer.')
        self.comendo = False
    
    # Quando a variavel self é um booleano(True or False) devesse criar 2 metodos(um que coloque ele em True e outro que coloque-o em False)
    def falar(self,assunto):
        if self.comendo == True:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando == True:
            print(f'{self.nome} já está falando sobre algo')
            return 

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if self.falando == True:
            print(f'{self.nome} não está mais falando')
            self.falando = False
            return
        
        



        