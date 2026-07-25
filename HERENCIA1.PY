class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}")

class Diseñador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje):
        super().__init__(nombre, edad, salario)
        self.lenguaje = lenguaje

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje: {self.lenguaje}")

class Programador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje):
        super().__init__(nombre, edad, salario)
        self.lenguaje = lenguaje
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Lenguaje: {self.lenguaje}")
        