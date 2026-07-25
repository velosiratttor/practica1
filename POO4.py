class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")  
        
person1 = Persona("Juan", 30)
person1.mostrar_informacion()