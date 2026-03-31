#ANDRES LOPEZ 20251678011
print("Bienvenido al sistema de conteo y registro mensual ACMUD!")
presupuesto = int(input("Para empezar defina cual es su presupuesto para este mes:"))
contador = 1
Transporte=[]
Comida=[]
entretenimiento=[]
emergencias=[]
totaldia =0
total=[]
ropa=[]
while contador<32:
    
    print(f"Escriba una opcion, estamos en el dia {contador}")
    print("Escriba 1 para añadir un gasto de tipo transportes")
    print("Escriba 2 para añadir un gasto de tipo comida")
    print("Escriba 3 para añadir un gasto de tipo entretenimiento")
    print("Escriba 4 para añadir un gasto de tipo ropa")
    print("Escriba 5 para añadir un gasto de tipo emergencias")
    print("Escriba 8 para avanzar al dia de mañana")
    print("Escriba 9 para terminar el registro ")
    opcion = int( input())
    if opcion ==1:
        print("Escriba cuanto gasto hoy en transportes (taxis,sitp, uber etc..)")
        valor = int(input())
        Transporte.append(valor)
        print("Registro guardado!")
        totaldia= totaldia+valor
    elif opcion==2:
        print("Escriba cuanto gasto hoy en comida (desayunos, almuerzos y cenas)")
        valor = int(input())
        Comida.append(valor)
        print("Registro guardado!")
        totaldia= totaldia+valor
    elif opcion==3:
        print("Escriba cuanto gasto hoy en entretenimiento(juegos, peliculas)")
        valor = int(input())
        entretenimiento.append(valor)
        print("Registro guardado!")
        totaldia= totaldia+valor
    elif opcion==4:
        print("Escriba cuanto gasto hoy en ropa")
        valor = int(input())
        ropa.append(valor)
        print("Registro guardado!")
        totaldia= totaldia+valor
    elif opcion==5:
        print("Escriba cuanto gasto hoy en emergencias ")
        valor = int(input())
        emergencias.append(valor)
        print("Registro guardado!")
        totaldia= totaldia+valor
    elif opcion ==8:
        print(f"Total gastado hoy {totaldia}")
        total.append(totaldia)
        contador = contador +1
        totaldia=0
    elif opcion==9:
        if len(total)<contador:
             total.append(totaldia)
             contador = contador +1
             totaldia=0
        contador = 32
contador=1
totaltransporte = 0
totalcomida=0
totalentrete = 0
totalemergencias = 0
totalropa =0
totalmes = 0

for i in Transporte:
    totaltransporte =  totaltransporte + i 
for i in Comida:
    totalcomida =  totalcomida + i 
for i in entretenimiento:
    totalentrete =  totalentrete + i 
for i in emergencias:
    totalemergencias =  totalemergencias + i 
for i in ropa:
    totalropa =  totalropa + i 
for i in total:
    print(f"En el dia {contador} se gasto un total de : {i} $")
    contador =contador+1
    totalmes = totalmes + i

print(f"TOTAL GASTADO EN ROPA: {totalropa}")
print(f"TOTAL GASTADO EN TRANSPORTE: {totaltransporte}")
print(f"TOTAL GASTADO EN ENTRENMIENTO : {totalentrete}")
print(f"TOTAL GASTADO EN COMIDA: {totalcomida}")
print(f"TOTAL GASTADO EN EMERGENCIAS: {totalemergencias}")
print(f"TOTAL GASTADO EN EL MES {totalmes}")
if totalmes>presupuesto:
    print(f"Segun tu presupuesto planeado, gastaste de mas, y ahora tienes un deficit del {(presupuesto-totalmes)}")
else:
    print(f"Segun tu presupuesto planeado. has ahorrado dinero y te has ahorrado : {(presupuesto-totalmes)}") 

