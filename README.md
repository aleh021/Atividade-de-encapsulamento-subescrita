#Passo 01
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome (self, nome):
        self.__nome = nome
#Passo 02,03,04,05,06
class Pessoa:
    def __init__(self, nome):
        self.__nome = nome
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome (self, novo_nome):
        self.__nome = novo_nome

nome_digitado = input("Digite o nome da pessoa: ")
pessoa = Pessoa(nome_digitado)
print("Pessoa criada com o nome:", pessoa.nome)
novo_nome_digitado = input("Digite o novo nome da pessoa: ")
pessoa.nome = novo_nome_digitado
print("Nome da pessoa alterado para:", pessoa.nome)
print("Nome da pessoa:", pessoa.nome)
