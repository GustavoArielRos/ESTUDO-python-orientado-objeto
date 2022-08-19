# Importando a classe

from pessoa import Pessoa
from pessoa2 import Pessoa2

#atribuindo a classe numa variável
#p1 = Pessoa()
#p2 = Pessoa()

# p1 != p2

#p1 = Pessoa('Luiz', 29) # quando tem parametro tu tem que colocar valor aqui

#quando não tem parametro na função tu coloca assim

#p1.nome = 'Luiz'
#p1.idade = 29

# Primeiro você deve atribuir a classe com os seu parametros numa variável
p3 = Pessoa('Carlos',22)

# Para usar os metodos(funções) da classe
p3.jantando('arroz')
p3.parar_jantar()
p3.falar('politica')
p3.parar_falar()

p4 = Pessoa2('Tadeu',33)

print(p4.get_ano_nasc())