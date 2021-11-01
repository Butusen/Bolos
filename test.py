import unittest
from Bolos import Bolos


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
        self.assertEqual(resultado, 20+13+3+3)

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

    def test_partida_con_spare_strike_spare(self):
        partida = Bolos()
        ronda = [(5, 5), (10, 0), (6, 4), (3, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = partida.calcularpuntuacion(ronda)
        self.assertEqual(resultado, 20 + 20 + 13+4)
















if __name__ == '__main__':
    unittest.main()
