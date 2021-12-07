
class Bolos:
    def excepcion_mayor10(self, ronda):
        for i in range(0, len(ronda)):
            if (ronda[i][0] or ronda[i][1]) > 10:
                raise Bolosincorrectos
    def excepcion_negativos(self, ronda):
        for i in range(0, len(ronda)):
            if (ronda[i][0] or ronda[i][1]) < 0:
                raise Bolosincorrectos
    def sumamuyalta(self,ronda):
        for i in range(0, len(ronda)):
            if sum(ronda[i]) > 10:
                raise Bolosincorrectos
    def letrasno(self,ronda):
        for i in range(0, len(ronda)):
            if 'a' in ronda[i]:
                raise Letrasno
    def demasiadasrondas(self,ronda):
        if len(ronda) > 12:
            raise RondasdeMas
    def calcularpuntuacion(self,ronda):
        suma = 0
        try:
            if len(ronda) <= 12:
                for i in range(0, len(ronda)):
                    if i < 9:
                        if ronda[i][0] == 10:
                            if ronda[i+1][0] == 10:
                                suma = suma + sum(ronda[i]) + sum(ronda[i+1]) + ronda[i+2][0]
                            else: suma = suma + sum(ronda[i]) + sum(ronda[i+1])
                        elif sum(ronda[i]) == 10:
                            suma = suma + sum(ronda[i]) + ronda[i+1][0]
                        else:
                            suma = suma + sum(ronda[i])
                    elif i == 9:
                        suma = suma + sum(ronda[i])
                    else:
                        if sum(ronda[9]) == 10 and ronda[9][0] != 10:
                            suma = suma + ronda[9 + 1][0]
                        else:
                            suma = suma + sum(ronda[i])

            return suma
        except:
            print("error")

    def ganadorPartida(self,jugador1,jugador2):
        if jugador1 > jugador2:
            return jugador1
        elif jugador2 > jugador1:
            return jugador2
        elif jugador2 == jugador1:
            return "Empate"

class Bolosincorrectos(Exception):
    pass
class RondasdeMas(Exception):
    pass
class Letrasno(Exception):
    pass