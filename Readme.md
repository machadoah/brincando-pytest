# Pytest 

Video: [Pytest: Uma introdução - Live de Python #167](https://www.youtube.com/live/MjQCvJmc31A?si=eTIffGkhbUP1Pi82)

Pytest é um framework em python dedicado a testes. Um alternativa mais "pythonica" ao unittest.

- Simples
- Escalável
- Rico em plugins
- Suporte ao pypy
- Primeira release em 2009
- Atualmente na versão [8.2.x](https://docs.pytest.org/en/8.2.x/)

### Executar

```
pytest -v test_pytest.py
```
> [!NOTE]
> O `-v` (verbose) descreve de maneira detalhada o código.

### Como vamos práticar?

Vamos um número inteiro, por exemplo "1":

- Quando o número foi **multiplo de 3**, deve responder **Queijo**. 
- Quando o número foi **multiplo de 5**, deve responder **Goiabada**.
- Quando o número foi **multiplo de 3 e 5**, deve responder **Romeu e Julieta**.