#Azul Fernanda Hernández García
# Grupo: 951
# Fecha: 30 de agosto de 2026
# Descripción: Sistema de encriptación y desencriptación de mensajes secretos
# utilizando un diccionario que asigna a cada letra del abecedario un código
# alfanumérico aleatorio de 3 caracteres, generado con el módulo random.
# Incluye una función para encriptar un mensaje (sustituyendo cada letra por
# su código) y otra para desencriptarlo (recuperando la letra original a
# partir de su código).


import random

abecedario="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
caracteres="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"

diccionario_encriptacion={}

for letra in abecedario:
    codigo= ""
    for i in range(3):
        codigo=codigo+random.choice(caracteres)
    diccionario_encriptacion[letra]=codigo

print(diccionario_encriptacion)

def encriptar_mensaje(mensaje):
    mensaje_encriptado= ""
    for letra in mensaje:
        mensaje_encriptado=mensaje_encriptado+diccionario_encriptacion[letra]
    return mensaje_encriptado

def desencriptar_mensaje(mensaje_encriptado):
    mensaje_desencriptado=""
    for i in range(0,len(mensaje_encriptado),3):
        codigo_actual=mensaje_encriptado[i:i+3]
        for letra, valor in diccionario_encriptacion.items():
            if valor==codigo_actual:
                mensaje_desencriptado=mensaje_desencriptado+letra
    return(mensaje_desencriptado)



if __name__ == "__main__":
    print("Mensaje Encriptado")
    encriptacion = encriptar_mensaje("Money")
    print(encriptacion)
    print("-----------------------------------------------------")
    print("Mensaje Desencriptado")
    desencriptacion=desencriptar_mensaje(encriptacion)
    print(desencriptacion)


