def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def x(a, b):
    return a+5 * b*8


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação e = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20
exibir_resultado (10, 10, subtrair)
exibir_resultado (10, 10, x)

op = somar
print(op(2,36))