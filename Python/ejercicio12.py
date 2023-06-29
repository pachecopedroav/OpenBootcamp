paises = input("Introduce países, separados por comas: ")

paises = sorted(list(set(paises.split(","))))

for i in range(len(paises)):
    paises[i] = paises[i].strip()

print(', '.join(paises))
