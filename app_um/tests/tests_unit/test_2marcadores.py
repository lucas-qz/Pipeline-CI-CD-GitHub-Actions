# A1 - CRIANDO TESTES
from pytest import mark


@mark.teste1  # A2 A3 A4 A5
def test_com_marcador_teste1_a():
    assert (1, 2, 3) == (1, 2, 3)


@mark.teste1  # A2 A3 A4 A5
def test_com_marcador_teste1_b():
    assert (1, 2, 3) == (1, 2, 3)


@mark.skip  # A6
def test_com_marcador_skip():
    assert (1, 2, 3) == (1, 2, 3)


@mark.skip(reason=">>pulei esse teste porque eu quis<<")  # A7
def test_com_marcador_skip_com_reason():
    assert (1, 2, 3) == (1, 2, 3)


a = 10  # A8


@mark.skipif(a > 0, reason='>>só vou pular se "a" for maior que zero<<')
def test_com_marcador_skipif():
    assert (1, 2, 3) == (1, 2, 3)


@mark.parametrize("entrada", [3, 5, 6])  # A9
def test_com_marcador_parametrize_multiplas_entradas(entrada):
    assert (entrada) == (entrada)


@mark.parametrize("entr1,entr2", [(2, 4), (7, 1), (1, 2)])  # A10
def test_com_marcador_parametrize_multiplas_parametrizacoes_2_paramentros(entr1, entr2):
    assert (entr1, entr2) == (entr1, entr2)


@mark.parametrize("entr1,entr2,entr3", [(2, 4, 6), (7, 1, 5), (1, 2, 9)])  # A11
def test_com_marcador_parametrize_multiplas_parametrizacoes_3_paramentros(
    entr1, entr2, entr3
):
    assert (entr1, entr2, entr3) == (entr1, entr2, entr3)


@mark.xfail  # A12
def test_com_marcador_xfail_a():
    assert (1, 2, 3) == (5, 2, 3)  # esse teste deve FALHAR


@mark.xfail  # A12
def test_com_marcador_xfail_b():
    assert (1, 2, 3) == (1, 2, 3)  # esse teste deve PASSAR


b = 10


@mark.xfail(b > 0, reason='>>mostrar com XFAIL só se "b" for maior que zero<<')  # A13
def test_com_marcador_xfail_a():
    assert (1, 2, 3) == (5, 2, 3)  # esse teste deve FALHAR


@mark.xfail(b > 0, reason='>>mostrar com XFAIL só se "b" for maior que zero<<')  # A13
def test_com_marcador_xfail_b():
    assert (1, 2, 3) == (1, 2, 3)  # esse teste deve PASSAR


# A2 - RODAR SOMENTE TESTES QUE ESTÃO USANDO DETERMINADO MARCADOR
# - coloque o marcador encima das funções de teste que deseja selecionar ('teste1' é um exemplo, pode ser qualquer nome)
# - no explo abaixo, serão rodados somente os testes q contem o marcador @mark.teste1 (é semelhante ao uso da Flag -k)
# 	@mark.teste1
# 	def test_nome_1() ...
# 	@mark.teste1
# 	def test_nome_2() ...
# - COMANDO NORMAL:      pytest --tb=no -m teste1     ('teste1' é o nome do marcador)
# - COMANDO COM VERBOSE: pytest --tb=no -v -m teste1  ('teste1' é o nome do marcador)

# A3 - REMOVENDO OS WARNINGS ------
# *na resposta dos testes as vezes aparece um trecho ==== warnings summary ===== com diversas informações. Para não mostrar esse trecho:
# - Crie na raiz do projeto um arquivo 'pytest.ini' com o codigo:
# [pytest]
# filterwarnings =
#     error
#     ignore::UserWarning
#     ignore:function ham\(\) is deprecated:DeprecationWarning
# ---------------------------------

# A4 - REFAÇA O TESTE ANTERIOR E VEJA QUE NÃO MOSTRA MAIS OS WARNINGS
# - COMANDO NORMAL:      pytest --tb=no -m teste1     ('teste1' é o nome do marcador)
# - COMANDO COM VERBOSE: pytest --tb=no -v -m teste1  ('teste1' é o nome do marcador)

# A5 - RODAR SOMENTE TESTES QUE NÃO ESTÃO USANDO DETERMINADO MARCADOR
# *no explo abaixo, serão rodados somente os testes q NÃO CONTEM o marcador @mark.teste1
# - COMANDO NORMAL:      pytest --tb=no -m "not teste1"     ('teste1' é o nome do marcador)
# - COMANDO COM VERBOSE: pytest --tb=no -v -m "not teste1"  ('teste1' é o nome do marcador)

# A6 - PULAR TESTES COM MARCADOR 'SKIP'
# *qndo chegar nesse teste ele vai pular, ou seja, não vai executa-lo
# *se no 'skip' tiver uma 'reason', ela será exibida
# 	@mark.skip
# 	def test_nome_1() ...
# 	@mark.skip(reason="escreva aqui um motivo pq deseja pular esse teste")
# 	def test_nome_1() ...
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v

# A7 - PULAR TESTES COM MARCADOR 'SKIP' e COM (FLAG -rs)
# *usando a Flag -rs ele mostra uma area exclusiva p as 'reason'. PORÉM essa área fica no lugar da area com as informações sobre as FALHAS
# - COMANDO NORMAL:      pytest --tb=no -rs
# - COMANDO COM VERBOSE: pytest --tb=no -v -rs

# A8 - PULAR TESTES COM MARCADOR 'SKIP IF'
# *qndo chegar nesse teste ele vai pular, MAS conforme a condição que está dentro de skipif()
# *no explo abaixo, vai pular esse teste de a variavel 'a' for maior que 0
# 	a=10
# 	@mark.skipif(a>0,reason='escreva aqui um motivo pq deseja pular esse teste')
# 	def test_nome_1() ...
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v

# A9 - MARCADOR 'PARAMETRIZE' - MULTIPLAS ENTRADAS
# *esse marcador nos permite executar o mesmo teste com diversos valores diferentes de Entrada
# *no explo abaixo a função 'def' recebe os parametros assim: no 1º teste recebe valor '3', no segundo teste recebe o valor '5', etc
# 	@mark.parametrize( 'entrada', [3,5,6,8,9,2] )
# 	def test_nome_1(entrada) ...
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v

# A10 - MARCADOR 'PARAMETRIZE' - MULTIPLAS PARAMETRIZAÇÕES - 2 PARAMETROS
# *esse marcador nos permite executar o mesmo teste com diversos valores diferentes de Entrada
# *no explo abaixo a função 'def' recebe os parametros assim: no 1º teste recebe valor '2,4', no segundo teste recebe o valor '7,1', etc
# 	@mark.parametrize( 'entr1,entr2', [(2,4),(7,1),(1,2),(9,18)] )
# 	def test_nome_1(entr1,entr2) ...
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v

# A11 - MARCADOR 'PARAMETRIZE' - MULTIPLAS PARAMETRIZAÇÕES - 3 PARAMETROS
# *esse marcador nos permite executar o mesmo teste com diversos valores diferentes de Entrada
# *no explo abaixo a função 'def' recebe os parametros assim: no 1º test recebe valor '2,4,6', no segundo test receb o valor '7,1,2', etc
# 	@mark.parametrize( 'entr1,entr2,entr3', [(2,4,6),(7,1,2),(1,2,5),(9,18,27)] )
# 	def test_nome_1(entr1,entr2,entr3) ...
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v

# A12 - TESTANDO FALHAS COM MARCADOR 'xFAIL'
# *imagine q por algum motivo criei um ou mais testes q espero que falhem. Como enxergar isso? É para isso q serve o marcador @mark.xfail
# * Se o teste de falha Falhou, vc vai enxerga-lo assim na resposta --> XFAIL (cor amarela)
# * Se o teste de falha Passou, vc vai enxerga-lo assim na resposta --> XPASS (cor amarela)
# 	@mark.xfail
# 	def test_nome_1() ...
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v

# A13 - MARCADOR 'xFAIL' COM CONDIÇÃO
# *imagine q por algum motivo criei um ou mais testes q espero que falhem. Como enxergar isso? É para isso q serve o marcador @mark.xfail
#  POREM TEM UM DETALHE, só quero enxergar essas falhas com o marcador 'xFAIL' se, por Ex, o teste estiver rodando apartir do Windows
# * Se rodou em um Windows     --> Se o teste de falha Passou, vc vai enxerga-lo assim na resposta --> XPASS  (cor amarela)
#                              --> Se o teste de falha Falhou, vc vai enxerga-lo assim na resposta --> XFAIL  (cor amarela)
# * Se NÃO rodou em um Windows --> Se o teste de falha Passou, vc vai enxerga-lo assim na resposta --> PASSED (cor verde)
#                              --> Se o teste de falha Falhou, vc vai enxerga-lo assim na resposta --> FAIL   (cor vermelha)
# 	@mark.xfail(sys.platform.startswith("win"),reason='escreva aqui oq desejar')
# 	def test_nome_1() ...
# --- TESTE 1 - coloque varaivel b = 10  ---> na resposta vai mostrar assim (XFAIL  e XPASS)
# --- TESTE 2 - coloque varaivel b = -10 ---> na resposta vai mostrar assim (FAILED e PASSED)
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v
