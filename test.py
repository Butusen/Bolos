import unittest
from Bolos import Bolos, Bolosincorrectos,RondasdeMas,Letrasno


class MyTestCase(unittest.TestCase):
    def crearPartida(self):
        partida = Bolos()

    def test_partida_suma_cero(self):
        partida = Bolos()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 0)

    def test_partida_suma_dos(self):
        partida = Bolos()
        ronda = [(2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 2)

    def test_partida_suma_tres_misma_ronda(self):
        partida = Bolos()
        ronda = [(0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 3)

    def test_partida_suma_diez_diferentes_rondas(self):
        partida = Bolos()
        ronda = [(4, 1), (2, 1), (2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 10)
    def test_partida_con_un_strike(self):
        partida = Bolos()
        ronda = [(10, 0), (2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 14)
    def test_partida_con_dos_strikes_separados(self):
        partida = Bolos()
        ronda = [(10, 0), (2, 0), (10, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 12+2+13+3)
    def test_partida_con_dos_strikes_juntos(self):
        partida = Bolos()
        ronda = [(10, 0), (10, 0), (2, 1), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 22+13+3+3)

    def test_partida_con_spare(self):
        partida = Bolos()
        ronda = [(4, 6), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 12+3)

    def test_partida_con_dos_spare_separados(self):
        partida = Bolos()
        ronda = [(4, 6), (2, 1), (5, 5), (4, 3), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 12+3+14+7)

    def test_partida_con_dos_spare_juntos(self):
        partida = Bolos()
        ronda = [(4, 6), (5, 5), (4, 3), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 15+14+7)

    def test_partida_con_strike_spare_seguidos(self):
        partida = Bolos()
        ronda = [(10, 0), (5, 5), (6, 3), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 20+16+9)

    def test_partida_con_strike_strike_spare(self):
        partida = Bolos()
        ronda = [(10, 0), (10, 0), (6, 4), (5, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 26+20+15+6)

    def test_partida_con_spare_strike_spare(self):
        partida = Bolos()
        ronda = [(5, 5), (10, 0), (6, 4), (3, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 20 + 20 + 13+4)

    def test_partida_con_cinco_strikes_juntos(self):
        partida = Bolos()
        ronda = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 30+30+30+22+13+3)

    def test_partida_con_ronda_extra(self):
        partida = Bolos()
        ronda = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (2, 1), (0, 0), (0, 0), (0, 0), (5, 5), (4, 5)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 30+30+30+22+13+3+14)

    def test_partida_con_rondas_extra(self):
        partida = Bolos()
        ronda = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (2, 1), (0, 0), (0, 0), (0, 0), (10, 0), (10, 0), (10, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 30+30+30+22+13+3+30)

    def test_partida_perfecta(self):
        partida = Bolos()
        ronda = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (10, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 300)

    def test_partida_con_ronda_extra_spare2(self):
        partida = Bolos()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(15,resultado)

    def test_excepcion_mayor10(self):
        partida = Bolos()
        ronda = [(11, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5)]
        try:
            partida.excepcion_mayor10(ronda)
        except Bolosincorrectos:
            pass
        else:
            self.fail("mierda")
    def test_excepcion_negativos(self):
        partida = Bolos()
        ronda = [(-1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5)]
        try:
            partida.excepcion_negativos(ronda)
        except Bolosincorrectos:
            pass
        else:
            self.fail("mierda")


    def test_demasiadas_rondas(self):
        partida = Bolos()
        ronda = [(10, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (3,0),(3,0), (3,0), (3,0)]
        try:
            partida.demasiadasrondas(ronda)
        except RondasdeMas:
            pass
        else:
            self.fail("caca")
    def test_sumamuyalta(self):
        partida = Bolos()
        ronda = [(10, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5)]
        try:
            partida.sumamuyalta(ronda)
        except Bolosincorrectos:
            pass
        else:
            self.fail("caca")
    def test_letrasNo(self):
        partida = Bolos()
        ronda = [(10, 0), (0, 0), (0, 'a'), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5)]
        try:
            partida.letrasno(ronda)
        except Letrasno:
            pass
        else:
            self.fail("caca")
    def test_partida_gana_2(self):
        partida= Bolos()
        ronda1 = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        ronda2 = [(4, 5), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        jugador1 = partida.calcularpuntuacion(ronda1)
        jugador2 = partida.calcularpuntuacion(ronda2)
        ganador = partida.ganadorPartida(jugador1,jugador2)
        self.assertEqual(jugador2,ganador)

    def test_partida_gana_1(self):
        partida = Bolos()
        ronda1 = [(6, 4), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        ronda2 = [(4, 5), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        jugador1 = partida.calcularpuntuacion(ronda1)
        jugador2 = partida.calcularpuntuacion(ronda2)
        ganador = partida.ganadorPartida(jugador1, jugador2)
        self.assertEqual(jugador1, ganador)

    def test_partida_empate(self):
        partida = Bolos()
        ronda1 = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        ronda2 = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (5, 5), (5, 2)]
        jugador1 = partida.calcularpuntuacion(ronda1)
        jugador2 = partida.calcularpuntuacion(ronda2)
        ganador = partida.ganadorPartida(jugador1, jugador2)
        self.assertEqual("Empate", ganador)


if __name__ == '__main__':
    unittest.main()
