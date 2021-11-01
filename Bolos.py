class Bolos:

    def calcularpuntuacion(self,ronda):
        suma = 0
        for i in range(0, len(ronda)):
            if ronda[i] [0] == 10:
                if ronda[i+1] [0] == 10:
                    suma = suma + sum(ronda[i]) + sum(ronda[i+1]) + ronda[i+2] [0]
                else: suma = suma + sum(ronda[i]) + sum(ronda[i+1])
            elif sum(ronda[i]) == 10:
                suma = suma + sum(ronda[i]) + ronda[i+1] [0]
            else:    suma = suma + sum(ronda[i])
        return suma



