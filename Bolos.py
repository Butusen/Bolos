class Bolos:

    def calcularpuntuacion(self,ronda):
        suma = 0
        for i in range(0, len(ronda)):
            if ronda[i] [0] == 10:
                suma = suma + sum(ronda[i]) + sum(ronda[i+1])
            else:    suma = suma + sum(ronda[i])
        return suma



