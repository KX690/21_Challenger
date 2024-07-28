class Figura:
    def imprimir(self,figura):
        print(f"Esto es una {figura}")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def imprimir(self):
        area= self.radio*self.radio*3,14
        print(f"El area del circulo es {area}.")


figura1=Figura()
figura1.imprimir("Esfera")

circulo = Circulo(int(input("Intruduzca un radio: ")))
circulo.imprimir()
