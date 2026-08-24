#EJERCICIO 1: ESTADÍSTICA BÁSICA
#Nombre: Azul Hernandez Garcia
#Grupo: 951
#Fecha de realización: 23 de agosto de 2026
#Descripción del problema: Crear una clase que calcule frecuencia, moda e
#imprima un histograma de una lista de números naturales.

class Estadistica:
    def __init__(self, lista):
        self.lista=lista
    def frecuencia(self):
        resultado=[]
        for numero in self.lista:
            encontrado=False
            for i in range(len(resultado)):
                if resultado[i][0]==numero:
                    resultado[i]=(numero, resultado[i][1]+1)
                    encontrado=True
                    break
            if not encontrado:
                resultado.append((numero,1))
        return resultado


    def moda(self):
        frecuencias=self.frecuencia()
        moda_tupla=frecuencias[0]
        for tupla in frecuencias:
            if tupla[1]>moda_tupla[1]:
                moda_tupla=tupla
        return moda_tupla[0]

    def histograma(self):
        frecuencias=self.frecuencia()
        for numero,veces in frecuencias:
            print(numero, "*" * veces)

if __name__ == "__main__":
    lista=Estadistica([1,3,2,4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
    print("Frecuencia:",lista.frecuencia())
    print("-----------------------------------------------------")
    print("la moda es:",lista.moda())
    print("-----------------------------------------------------")
    print("Histograma")
    lista.histograma()
    print("-----------------------------------------------------")
    print("Fin :D")
