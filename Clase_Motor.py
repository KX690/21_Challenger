class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def describir(self):
        return f"El motor es {self.tipo}, con una potencia de potencia: {self.potencia} HP"

class Auto:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir_auto(self):
        return f"Es de la marca {self.marca}, y modelo {self.modelo}, {self.motor.describir()}"

motor = Motor(input("Introduzca el tipo de motor"), int(input("Introduzca la potencia del motor")))
auto = Auto("Toyota", "Izusu", motor)
print(auto.describir_auto())
