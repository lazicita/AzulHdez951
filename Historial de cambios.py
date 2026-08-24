#EJERCICIO 2: HISTORIAL DE CAMBIOS (PILA)
#Nombre: Azul Hernandez Garcia
#Grupo: 951
#Fecha de realización: 24 de agosto de 2026
#Descripción del problema: Simular un historial de cambios tipo "Deshacer"
#usando una lista como pila (LIFO).

def registrar_cambios(historial, celda, valor):
    historial.append((celda, valor))

def deshacer_cambios(historial):
    if historial:
        return historial.pop()
    else:
        print("No hay cambios para deshacer :>")
        return None

#Simulacion
historial_cambios=[]

registrar_cambios(historial_cambios,  'A1', 10)
registrar_cambios(historial_cambios, 'B2', 20)
print("Resultado 1")
print(historial_cambios)
print("---------------------------------")
deshacer_cambios(historial_cambios)
print("Resultado 2")
print(historial_cambios)
print("----------------------------------")
print("Fin :D")