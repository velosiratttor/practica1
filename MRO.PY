class A:

    def saludar(self):
        print("Hola desde A")


class B:

    def saludar(self):
        print("Hola desde B")


class C(B, A):
    pass


obj = C()

obj.saludar()