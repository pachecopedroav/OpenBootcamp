class Alumno:

    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
               print(f"Nombre: {self.nombre}")
               print(f"Nota: {self.nota}")

    def resultado(self):
            if self.nota < 60:
                print(f"{self.nombre} ha reprobado")
            else:
                print(f"{self.nombre} ha aprobado")
 
 
pedro = Alumno()
luis = Alumno()
 
pedro.inicializar("Pedro", 96)
luis.inicializar("Luis", 55)

pedro.imprimir_datos()
pedro.resultado()

luis.imprimir_datos()
luis.resultado()
