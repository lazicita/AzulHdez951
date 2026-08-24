#EJERCICIO 3: NAVEGACIÓN EN ALMACÉN
#Nombre: Azul Hernandez Garcia
#Grupo: 951
#Fecha de realización: 24 de agosto de 2026
#Descripción del problema: Verificar si un robot recoge todos los productos 'P'
#y regresa al inicio (0,0) sin chocar, siguiendo una lista de movimientos.
#Nota: L (Izquierda) y U (Arriba) solo se activan para el retorno.

almacen = [
[ '.',  '.',  '#',  'P'],
[ '.',  '#',  '.',  '.'],
[ 'P',  '.',  'P',  '.'],
[ '#',  '.',  '#',  '.']
     		       ]
def verificar_recogida_productos(almacen,movimientos_correctos):
    total_p = 0
    for item in range(len(almacen)):
        for item2 in range(len(almacen[item])):
            if almacen[item][item2]=="P":
                total_p+=1
    fila=0
    columna=0
    posiciones_guardadas=set()
    for movimiento in movimientos_correctos:
        if movimiento=="D":
            nueva_fila=fila+1
            nueva_columna=columna
        elif movimiento=="R":
            nueva_fila=fila
            nueva_columna=columna+1
        elif movimiento=="L":
            nueva_fila=fila
            nueva_columna=columna-1
        elif movimiento=="U":
            nueva_fila=fila-1
            nueva_columna=columna
        else:
            print("Error: Movimiento no valido")
        if nueva_fila<0 or nueva_fila>=len(almacen):
            return False
        if nueva_columna <0 or nueva_columna>=len(almacen[0]):
            return False
        if almacen[nueva_fila][nueva_columna]=="#":
            return False
        fila=nueva_fila
        columna=nueva_columna
        if almacen[fila][columna]=="P":
            posiciones_guardadas.add((fila,columna))
            print("Producto recogido en:","(",fila,",",columna,")")
    print("----------------------------------------------")
    print("Total de productos recogidos:",len(posiciones_guardadas))
    if fila==0 and columna==0 and len(posiciones_guardadas)==total_p:
        print("----------------------------------------------")
        return True
    else:
        return False
if __name__ == "__main__":
    movimientos_correctos = ['D', 'D', 'R', 'R', 'U', 'R', 'U', 'D', 'L', 'D', 'L', 'L', 'U', 'U']
    print(verificar_recogida_productos(almacen,movimientos_correctos))