class Banco:
    def __init__(self, nombre,saldo):
        self.nombre = nombre
        self.__saldo = saldo  # Atributo privado
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self,nuevo_saldo):
        if nuevo_saldo>=0:
            self.__saldo += nuevo_saldo
        
        elif nuevo_saldo<0:
            print("No se puede establecer un saldo negativo.")

banco1 = Banco("Banco de España", 1000000)

print(banco1.get_saldo())  # Output: 1000000
banco1.set_saldo(-500000)  # Output: No se puede establecer un saldo negativo.
banco1.set_saldo(500000)  # Aumenta el saldo en 500000
print(banco1.get_saldo())  # Output: 1500000