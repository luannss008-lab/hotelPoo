# class Animal():
#     def falar(self):
#         pass
#
# class Cachorro(Animal):
#     def falar(self):
#         print('auau')
# comando = Cachorro()
# comando.falar()

class Pessoa():
    def __init__(self, nome):
        self.nome = nome

class Estudante(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula


marcos = Estudante('Marcos',123)
print(marcos.matricula,marcos.nome)

