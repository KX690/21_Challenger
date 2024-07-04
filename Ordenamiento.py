arreglo=[7,21,33,5,1]

#mi auxiliar uso para el intercambio de datos con el metodo burbuja
aux=0


for i in range(5):
    for j in range(4):
        if(arreglo[j]>arreglo[j+1]):
            aux=arreglo[j]
            arreglo[j]=arreglo[j+1]
            arreglo[j+1]=aux
            

print(arreglo)