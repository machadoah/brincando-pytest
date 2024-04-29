from codigo.jogo import brincadeira

"""
o teste é formado por 3 etapas (GWT - AAA)

- given - dado
- when  - quando
- then  - então

- arange
- act
- assert
"""


def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1  # dado
    esperado = 1
    resultado = brincadeira(entrada)  # quando
    assert resultado == esperado  # então
    assert brincadeira(1) == 1  # então


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    entrada = 2  # dado
    esperado = 2
    resultado = brincadeira(entrada)  # quando
    assert resultado == esperado  # então


def test_quando_brincadeira_receber_3_entao_deve_retornar_goiaba():
    entrada = 3  # dado
    esperado = "queijo"
    resultado = brincadeira(entrada)  # quando
    assert resultado == esperado  # então
