



class Cuenta:
    def __init__(self):
        self.importe_inicial=90000
        self.total=self.importe_inicial
    def Consultar(self):
        print(f"El dinero total en la cuenta es: {self.total} ")
    
    def Depositar(self, dinero):
        self.total+=dinero
        print(f"El dinero actual es {self.total}")
        
    def Menu(self):
        print("""
              Elija una opcion
              1. Depositar
              2. Consultar
              3. salir
              """)
        opcion =int(input("Opcion: "))
        return opcion
    
cajero=Cuenta()
opcion=cajero.Menu()
while(opcion!=3):
    if(opcion==1):
        cajero.Depositar(int(input("Introduzca el monto a depocitar: ")))
    elif(opcion ==2):
        cajero.Consultar()
    
    opcion=cajero.Menu()
    
    

        