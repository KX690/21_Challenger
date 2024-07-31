from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

class Rectangulo(FormaGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        print(f"Área del rectángulo: {area}")
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        print(f"Perímetro del rectángulo: {perimetro}")

class Circulo(FormaGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = 3.14 * (self.radio ** 2)
        print(f"Área del círculo: {area}")

    def calcular_perimetro(self):
        perimetro = 2 * 3.14 * self.radio
        print(f"Perímetro del círculo: {perimetro}")
        
        
base=int(input("Introduzca la base para el rectangulo: "))
altura=int(input("Introduzca la altura para el rectangulo: "))
figura1=Rectangulo(base,altura)
figura1.calcular_area()
figura1.calcular_perimetro()

radio=int(input("Introduzca un radio para la circunferencia: "))
figura2 = Circulo(3)
figura2.calcular_area()
figura2.calcular_perimetro()