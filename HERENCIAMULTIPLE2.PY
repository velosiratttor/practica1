class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
class Empleado:
    def __init__(self, nombre, edad, salario):
        self.persona = Persona(nombre, edad)
        self.salario = salario

    def mostrar_informacion(self):
        info_persona = self.persona.saludar()
        return f"{info_persona} Mi salario es {self.salario}."

class Diseñador(Persona,Empleado):
    def __init__(self, nombre, edad, salario, lenguaje):
        Persona.__init__(self, nombre, edad)
        Empleado.__init__(self, nombre, edad, salario)
        self.lenguaje = lenguaje

    def mostrar_informacion(self):
        info_empleado = Empleado.mostrar_informacion(self)
        return f"{info_empleado} Mi lenguaje de diseño es {self.lenguaje}."