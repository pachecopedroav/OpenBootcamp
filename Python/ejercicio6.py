class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):

    def __init__(self, velocidad, cilindrada, color, ruedas, puertas):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return f"Color {self.color}, {self.velocidad} km/h, {self.ruedas} ruedas, {self.puertas} puertas y {self.cilindrada} cc de cilindrada"

coche = Coche(200, 1800, "blanco", 4, 4)
print(coche)
