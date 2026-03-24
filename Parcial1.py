from sys import argv
d={} ##Diccionario vacio
dT={}
F=set()
def AFD(d,q0,F,cinta):
    q=q0
    for simbolo in cinta:
        q=d[q,simbolo]
    return q in F ##Retorna falso o verdadero, juzga si Q  esta en el estado final de aceptacion


direccion_global = ""

def MT(simbolo, estado):
    global direccion_global
    Nsimbolo, direccion_global = dT[estado, simbolo]
    siguiente_estado = d[estado, simbolo]
    simbolo = Nsimbolo
    if siguiente_estado in F:
        print("Aceptado")
    return simbolo, siguiente_estado

def Turing(programa):
    with open(programa) as programa:
        for linea in programa:
            estado, simbolo, operacion, direccion, nuevo = linea.split()
            if '*' in estado:
                estado = estado.strip('*')
                F.add(estado)     
            d[estado, simbolo] = nuevo
            dT[estado, simbolo] = (operacion, direccion)

    cinta = list(open(argv[2]).read().strip())  # leemos como lista de símbolos
    estado_actual = '0'
    cabeza = 0  # posición en la cinta

    while True:
        simbolo_actual = cinta[cabeza]
        simbolo_nuevo, estado_actual = MT(simbolo_actual, estado_actual)
        cinta[cabeza] = simbolo_nuevo

        if direccion_global == 'R':
            cabeza += 1
        elif direccion_global == 'L':
            cabeza -= 1

        if estado_actual in F:
            print("Aceptado, cinta final:", ''.join(cinta))
            break
    
       


def determinista(programa):
   with open(programa) as programa:
        for linea in programa:
            q, s, n = linea.split()
            if '*' in q:
                q = q.strip('*')
                F.add(q)
            d[q, s] = n
        mensaje = {True:'Aceptado', False:'Rechazado'}
        with open(argv[2]) as cintas:
            for cinta in cintas:
                cinta=cinta.strip()
                print('la entrada',cinta," es ", mensaje[AFD(d,'0',F, cinta)])


            

programa=open(argv[1])
primera_linea = programa.readline()
columnas = len(primera_linea.split()) 
    
print(f"La cantidad de columnas son: {columnas}")
if columnas == 3 :
    print("El programa es de maquina determinista")
    determinista(argv[1])
    programa.close()
elif columnas == 5:
    print("El programa es de maquina de Turing")
    Turing(argv[1])

programa.close()



