class Banco:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo  # Atributo privado
    def get_saldo(self):
        return self.__saldo
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("No se puede depositar una cantidad negativa.")
            
    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Saldo insuficiente.")
    def nuevo():
        pass

banco1 = Banco("Banco de España", 1000000)
banco1.depositar(500000)  # Aumenta el saldo en 500000
print(banco1.get_saldo())  # Output: 1500000
banco1.retirar(200000)  # Disminuye el saldo en 200000
print(banco1.get_saldo())  # Output: 1300000