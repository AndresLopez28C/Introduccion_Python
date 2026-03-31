#Andres Lopez 20251678011 - 1000580510
filai = int(input("Ingrese el numero para el rango inicial de filas :"))
filaf = int(input("Ingrese el numero para el rango final de filas: "))
columnai = int(input("Ingrese el numero para el rango inicial de columnas: "))
columnaf = int(input("Ingrese el numero para el rango final de columnas: "))
if filaf < filai or columnaf < columnai:
    print("Valores negativos para las dimensiones, intente de nuevo!!")

#print("hay ", filas, " y ", columnas, " columnas")
else:
    columnas = int(columnaf) - int(columnai) +2
    filas = int(filaf) - int(filai) +2
    matriz = []
    for i in range(filas):
        vacio = []
        for j in range(columnas):
            if i==0  and j == 0:
                vacio.append(1)
            else:
                if i==0:
                    vacio.append(columnai) ###La primera columna para definirrr
                    columnai+=1
                else:
                    if j==0:
                        vacio.append(filai)
                        filai+=1
                    else:
                        vacio.append(0)
        matriz.append(vacio)
        
    for x in range(filas):
        calculo = []
        for y in range(columnas):
            if x ==0 and y==0:
                pass
            else:
                matriz[x][y] = matriz[0][y] * matriz[x][0]
    matriz[0][0] = ''
    for m in matriz:
        print("\t",m)
