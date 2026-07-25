class Persona:
        
    def saludar(self):
        print("Hola, soy una persona.")

class Trabajador:
    def trabajar(self):
        print("Estoy trabajando.")
    
class Empleado(Persona, Trabajador):
    pass

empleado1 = Empleado()
empleado1.saludar()
empleado1.trabajar() 
