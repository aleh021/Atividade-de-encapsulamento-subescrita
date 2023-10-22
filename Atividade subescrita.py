class Integrante_IFRN:
    def exibirMensagem(self):
        return "Seja bem vindo(a) ao IFRN!!!"

class Professor(Integrante_IFRN):
    def exibirMensagem(self):
        return "Meus alunos são os melhores!!!"

class Aluno(Integrante_IFRN):
    def exibirMensagem(self):
        return "Vou estudar pra tirar 100 em POO!!!"

integrante = Integrante_IFRN()
professor = Professor()
aluno = Aluno()

print(integrante.exibirMensagem())
print(professor.exibirMensagem())
print(aluno.exibirMensagem())
