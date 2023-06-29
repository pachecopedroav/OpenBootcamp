import pickle # Para serializar y deserializar una estructura de objetos

class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def muestra_marca(self):
        print(f"El vehículo es: {self.marca}")

coche = Vehiculo("Toyota Corolla")
coche.muestra_marca()

# Crear fichero donde se va a serializar al objeto
file = open("vehiculo.bin", "wb")
pickle.dump(coche, file)
file.close()

# DESERIALIZAR
file2 = open("vehiculo.bin", "rb")
vehiculo = pickle.load(file2)
file2.close()

vehiculo.muestra_marca()
