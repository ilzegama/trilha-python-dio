salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


def funcao(*args, **kw):
  funcao("python", 2022, curso="dio")


salario_bonus(500)  # 2500
