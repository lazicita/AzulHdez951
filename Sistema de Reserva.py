#Azul Fernanda Hernández García
#Grupo: 951
#Fecha: 30 de agosto de 2026
#Descripción: Sistema de reservas de hotel utilizando sets para gestionar
#habitaciones disponibles y reservadas.

habitaciones=set([100,101,102,103,104,105,106,107,108,109,110])
reservadas=set([])
def reservas(numero_habitacion):
    if numero_habitacion in habitaciones:
        habitaciones.remove(numero_habitacion)
        reservadas.add(numero_habitacion)
        print("-----------------------------------------------------")
        print("La habitacion",numero_habitacion,"fue reservada con exito c:")
    elif numero_habitacion in reservadas:
        print("-----------------------------------------------------")
        print("La habitacion", numero_habitacion, "ya esta reservada :c")
    else:
        print("-----------------------------------------------------")
        print("La habitacion",numero_habitacion,"no existe :c")

def liberar_habitacion(habitacion_libre):
    if habitacion_libre in reservadas:
        reservadas.remove(habitacion_libre)
        habitaciones.add(habitacion_libre)
        print("-----------------------------------------------------")
        print("La habitacion",habitacion_libre,"fue liberada correctamente c:")
    else:
        print("-----------------------------------------------------")
        print("La habitacion",habitacion_libre,"ya estaba libre")

def mostrar_habitaciones():
    print("-----------------------------------------------------")
    print("Habitaciones Disponibles")
    for habitacion in habitaciones:
        print(habitacion)
    print("-----------------------------------------------------")
    print("Habitaciones Reservadas")
    for reservada in reservadas:
        print(reservada)
    print("-----------------------------------------------------")

if __name__ == "__main__":
    print("Caso 1: No hay ningun problema en reservar y liberar habitacion/es \n")
    reservas(100)
    mostrar_habitaciones()
    liberar_habitacion(100)
    mostrar_habitaciones()

    print("Caso 2: Se reserva una habitacion ya reservada \n")
    reservas(100)
    reservas(100)
    mostrar_habitaciones()

    print("Caso 3: Se intenta reservar una habitacion no existente \n")
    reservas(111)

    print("Caso 4: Se intenta liberar una habitacion que nunca fue reservada \n")
    liberar_habitacion(109)





