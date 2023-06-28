def conteo_inverso(inicio, fin):

    lista =  list(range(inicio, fin + 1))
    lista.sort(reverse= True)
    for num in lista:
        print(num)


conteo_inverso(1,100)
