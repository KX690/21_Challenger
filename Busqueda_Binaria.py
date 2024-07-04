
arreglo=[1,5,7,8,9,11,13,27,29,31,32]


numero=int(input("Introduzca el numero que desea buscar dentro de la lista: "))
minimo=0
maximo=len(arreglo)-1
pivot = int((minimo+maximo)/2)

b=True    

while(b):
    pivot=int((minimo+maximo)/2)
    if(numero==arreglo[pivot]):
        print(f"El numero se encuentra en el indice {pivot}")
        break
    elif(numero<arreglo[pivot]):
        maximo=pivot-1
        
        
    elif(numero>arreglo[pivot]):
        minimo=pivot+1
        
    
    if(minimo>maximo):
        print("El numero ingresado no esta en la lista")
        break    

