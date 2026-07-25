class Banco:
    def __init__(self, nombre,cantidad):
        self.nombre = nombre
        self.__cantidad = cantidad
    
    def get_cantidad(self):
        return self.__cantidad

banco1 = Banco("Banco de España", 1000000)

print(banco1.get_cantidad())  # Output: 1000000
banco1.__cantidad = 500000  # This will not change the private attribute
print(banco1.get_cantidad())  # Output: 1000000
