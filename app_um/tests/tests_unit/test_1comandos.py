# A1 - CRIANDO TESTES - QUEREMOS VALIDAR SE A TUPLA DA ESQUERDA É IGUAL A DA DIREITA
def test_que_passa1():  # - ESSE TESTE DEVE PASSAR
    assert (1, 2, 3) == (1, 2, 3)


"""
def test_que_falha():          # - ESSE TESTE DEVE FALHAR 
    print('>>esse vai Falhar<<')
    assert (1,2,3) == (1,2,93)
"""


def test_que_passa2():  # - ESSE TESTE DEVE PASSAR
    assert (1, 2, 3) == (1, 2, 3)


def test_que_passa3():  # - ESSE TESTE DEVE PASSAR
    assert (1, 2, 3) == (1, 2, 3)


# A2 - EXECUTAR TODOS OS TESTES
# - COMANDO NORMAL:      pytest
# - COMANDO COM VERBOSE: pytest -v

# A3 - ESCOLHENDO QUAL ARQUIVO DE TESTE EXECUTAR
# - COMANDO NORMAL:      pytest .\app_um\tests\tests_unit\test_1comandos.py
# - COMANDO COM VERBOSE: pytest .\app_um\tests\tests_unit\test_1comandos.py -v

# A4 - REMOVENDO TRACEBACKS - RESPOSTAS MAIS LIMPAS (FLAG --tb=no)
# - COMANDO NORMAL:      pytest --tb=no
# - COMANDO COM VERBOSE: pytest --tb=no -v

# A5 - FAZER O TESTE PARAR AO ENCONTRAR UMA FALHA (FLAG -x)
# - COMANDO NORMAL:      pytest --tb=no -x
# - COMANDO COM VERBOSE: pytest --tb=no -v -x

# A6 - ABRIR O MODO DEBUG AO ENCONTRAR UMA FALHA (FLAG ---pdb)
# - COMANDO NORMAL:      pytest --tb=no --pdb
# - COMANDO COM VERBOSE: pytest --tb=no -v --pdb
# *abre uma especie de terminal onde vc pode testar as variaveis do teste
# *para sair do modo debug digite 'q' e de ENTER

# A7 - RODAR TESTES ESPECIFICOS (FLAG -k)
# *no explo abaixo, serão rodados somente os testes q contem 'passa' no nome
# - COMANDO NORMAL:      pytest --tb=no -k "passa"
# - COMANDO COM VERBOSE: pytest --tb=no -v -k "passa"

# A8 - MOSTRAR PRINTS NO CONSOLE (FLAG -s)
# *se vc colocar um print no teste (antes de assert), podemos retorna-lo no teste com essa flag
# *o professor disse q não é uma boa pratica
# - COMANDO NORMAL:      pytest --tb=no -s
# - COMANDO COM VERBOSE: pytest --tb=no -v -s
