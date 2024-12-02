from django.shortcuts import render


def galeryview(request):
    return render(request, "gallery.html")


# A1 - Criando função que será testada no TESTE DE EXCEPTION PADRÃO
def dividir1(a, b):
    return a / b


# A2 - Criando função que será testada no TESTE DE EXCEPTION PERSONALIZADA
def dividir2(a, b):
    if b == 0:
        raise Exception(
            ">>Não pode dividir por zero<<"
        )  # criando uma exception personalizada
    return a / b


# B1 - Criando funções que serão testadas no TESTE EM CLASSES POO
def somar1(a, b):
    return a + b


def subtrair1(a, b):
    return a - b


# C1 - Criando a classe que será testada no TESTE COM FIXTURE PRONTA - capsys
class Retangulo:
    def __init__(self, largura=0, comprimento=0):
        self.largura = largura
        self.comprimento = comprimento
        print("criou retangulo")  # o print deve estar aqui no contrutor da Classe

    def calcula_area(self):  # metodo para calcular a area do objeto da classe Retangulo
        return self.largura * self.comprimento

    def novo_comprimento(
        self, novo_comp
    ):  # metodo para inputar novo valor ao atributo 'comprimento' do objeto da classe Retangulo
        self.comprimento = novo_comp


# D1 - criamos essa função e não criamos nenhum teste para ela - usaremos isso na COBERTURA DE TESTES AUTOMATIZADOS
def funcao_sem_teste():
    return print("sou uma função sem testes")
