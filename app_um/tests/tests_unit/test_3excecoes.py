from ... import views as vw  # A1 - importando tudo que está no arquivo 'views.py'
from pytest import mark, raises


# A1 - CRIANDO TESTES
def test_de_excecoes_padrao():  # A2
    a = 10
    b = 0
    with raises(
        ZeroDivisionError
    ):  # dicionamos esse tratamento para a exception de 'ZeroDivisionError'
        resposta = vw.dividir1(a, b)
        assert resposta


def test_de_excecoes_personalizadas():  # A3
    a = 10
    b = 0
    with raises(Exception):  # dicionamos esse tratamento para a exception personalizada
        resposta = vw.dividir2(a, b)
        assert resposta


# A2 - EXEMPLO DE EXCEPTION PADRÃO
# *qndo a função q vc está testando retorna uma Exception (EX: ZeroDivisionError), como fazer o teste Passar?
# *no arquivo de teste importe:   from pytest import mark, raises
# 	def test_nome_1()
# 	  with raises(ZeroDivisionError):                      # dicionamos esse tratamento para a exception de 'ZeroDivisionError'
# 		resposta = dividir_por_zero(5, 0)
# 		assert resposta
#   - TESTE-1 -----> rode os testes sem o tratamento para a exception e VEJA QUE o teste vai FALHAR
#   - TESTE-2 -----> rode os testes COM o tratamento para a exception e VEJA QUE o teste vai PASSAR
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v
# *o teste vai Passar, mesmo com essa Exception

# A3 - EXEMPLO DE EXCEPTION PERSONALIZADA
# --- NA FUNÇÃO
# def pense_num_numero(num):
#     if num <0:
#         raise Exception('Número precisa ser positivo!')    # criando uma exception personalizada
#     return num
#
# --- NO TESTE
# *no arquivo de teste importe:   from pytest import mark, raises
# def test_nome_2():
#     num = -1
#     with raises(Exception):                               # adicionamos esse tratamento para a Exception
#         resposta = pense_num_numero(num)
#         assert resposta
#   - TESTE-1 -----> rode os testes sem o tratamento para a exception e VEJA QUE o teste vai FALHAR
#   - TESTE-2 -----> rode os testes COM o tratamento para a exception e VEJA QUE o teste vai PASSAR
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v
# *o teste vai Passar, mesmo com essa Exception
