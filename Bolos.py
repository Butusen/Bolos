class Bolos:

    def calcularpuntuacion(self,ronda):
        suma = 0
        for i in ronda:
            valor1= i[0]
            valor2=i[1]
            suma = suma + valor1 +valor2
        return suma



