peso = float(input("¿Cuál es tu peso en kilogramos?: "))
estatura = float(input("¿Cuál es tu estatura en metros?: "))

imc = peso/estatura**2
imc_redondeado = round(imc, 2)
print(f"Tu índice de masa corporal es {imc_redondeado}")
