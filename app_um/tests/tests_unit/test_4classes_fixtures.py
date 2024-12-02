from ... import views as vw  # importando tudo que está no arquivo 'views.py'
from pytest import mark  # mark - serve pra usar mark
import pytest  # erve pra usar fixture


# A1 - CRIANDO TESTES
@mark.classeX  # A2 ---------------------------------------
class TestSoma:
    def test_com_classe_somar1(self):
        a = 2
        b = 2
        resultado = vw.somar1(a, b)
        assert resultado == (a + b)

    def test_com_classe_subtrair1(self):
        a = 2
        b = 2
        resultado = vw.subtrair1(a, b)
        assert resultado == (a - b)


def test_de_fixture_capsys(capsys):  # A3 ------------------------------
    retangulo = vw.Retangulo()
    resultado = (
        capsys.readouterr()
    )  # o print da classe fica armazenado em 'resultado.out'
    assert resultado.out == "criou retangulo\n"


@pytest.fixture  # A4 ------------------------------------------
def cria_retangulo7():  # criando uma FIXTURE PERSONALIZADA
    retangulo = vw.Retangulo(
        10, 5
    )  # essa Fixture instancia a classe 'Retangulo' (PORTANTO, ela é um objeto um objeto)
    return retangulo


def test_de_fixture_personalizada_teste_a(
    cria_retangulo7,
):  # uso a Fixture Personalizada aqui
    area = cria_retangulo7.calcula_area()
    assert area == 50


def test_de_fixture_personalizada_teste_b(
    cria_retangulo7,
):  # uso a Fixture Personalizada aqui
    cria_retangulo7.novo_comprimento(50)
    assert cria_retangulo7.comprimento == 50


# A2 - TESTES EM CLASSES POO
# *vc pode agrupar diversos testes dentro de uma Classe, então qndo testar a classe estará rodando todos os testes que estão nela
# *no arquivo de teste importe:   from pytest import mark
# *a classe deve sempre começar com 'Test'
# *qndo rodar os testes chamando esse marcador, ele roda tdos os tests q estão nessa Classe
# 	@mark.classeX                   # 'classeX' é o nome do marcador (vc escolhe qualquer nome)
# 	class TestNumeros:
# 	  def test_nome_1(self): ...    # tem que por 'self'
# 	  def test_nome_2(self): ...    # tem que por 'self'
# 	  def test_nome_3(self): ...    # tem que por 'self'
# - COMANDO NORMAL:      pytest --tb=no  -m classeX
# - COMANDO COM VERBOSE: pytest --tb=no -v  -m classeX


# A3 - FIXTURES PRONTAS
# LISTA DE FIXTURES PRONTAS - COMANDO: pytest --fixtures   (**na Aula só vimos a 'capsys')
#
# FIXTURE PRONTA - capsys (ela enxerga prints q estejam dentro de uma classe, função, etc)
# --- NA CLASSE
# *em uma classe, coloque um print no construtor da classe
# class Retangulo:
#     def __init__(self,largura=0,comprimento=0):
#         self.largura     = largura
#         self.comprimento = comprimento
#         print("criou retangulo")        # o print deve estar aqui no contrutor da Classe
# --- NO TESTE
# def test_de_fixture_capsys(capsys):
# 	retangulo = Retangulo()
# 	resultado = capsys.readouterr()     # o print da classe fica armazenado em 'resultado.out'
# 	assert resultado.out == "criou retangulo\n"
#
# - COMANDO NORMAL:      pytest .\app_um\tests\tests_unit\test_4classes_fixtures.py
# - COMANDO COM VERBOSE: pytest .\app_um\tests\tests_unit\test_4classes_fixtures.py -v
# - REPARE q o test PASSOU, já q oq foi salvo na Fixtures 'capsys' é realmente o print q ta na classe 'Retangulo', como era esperado


# A4 - FIXTURES PERSONALIZADAS
# *Fixtures Personalizadas servem para 'fazer uma preparação antes dos testes' e 'evitar repetição de codigos nos testes'
# *EX: Vc tem uma classe com 2 metodos. Vc tem um teste para cada metodo e ambos precisam instanciar a classe.
#      Ao inves d instanciar a classe 2 vezes vc cria uma Fixture q instancia essa classe e dpois vc só usa a Fixtures nos testes
#      Fazendo assim vc 'fez uma preparação antes dos testes' e 'evitou repetição de codigos nos testes'
# --- NA CLASSE
# class Retangulo:
#     def __init__(self,largura=0,comprimento=0):
#         self.largura     = largura
#         self.comprimento = comprimento
#         print("criou retangulo")          # o print deve estar aqui no contrutor da Classe
#     def calcula_area(self):               # metodo p calcular a area do objeto da classe Retangulo
#         return self.largura*self.comprimento
#     def novo_comprimento(self,novo_comp): # metodo p inputar novo valor ao atributo 'comprimento' do objeto da classe Retangulo
#         self.comprimento = novo_comp
# --- NO TESTE
# @pytest.fixture
# def cria_retangulo7():                     # criando uma FIXTURE PERSONALIZADA
#     retangulo = vw.Retangulo(10,5)         # essa Fixture instancia a classe 'Retangulo' (PORTANTO, ela é um objeto um objeto)
#     return retangulo
# def test_de_fixture_personalizada_teste_a(cria_retangulo7): # uso a Fixture Personalizada aqui
#     area = cria_retangulo7.calcula_area()
#     assert area == 50
# def test_de_fixture_personalizada_teste_b(cria_retangulo7): # uso a Fixture Personalizada aqui
#     cria_retangulo7.novo_comprimento(50)
#     assert cria_retangulo7.comprimento == 50
#
# - COMANDO NORMAL:      pytest .\app_um\tests\tests_unit\test_4classes_fixtures.py
# - COMANDO COM VERBOSE: pytest .\app_um\tests\tests_unit\test_4classes_fixtures.py -v
# - REPARE que os testes PASSARAM, como era esperado
