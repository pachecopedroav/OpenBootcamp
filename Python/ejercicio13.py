from functools import reduce

lista = [71, 2, 92, 28, 83, 93, 84, 92, 61, 39, 85, 17, 29, 40]

def esimpar(x):
    if x % 2 != 0:
        return True
    return False

lista_impar = list(filter(esimpar, lista))
print(lista_impar)

lista_reducida = reduce(lambda a, b: a + b, lista_impar)
print(lista_reducida)
