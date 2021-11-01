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











if __name__ == '__main__':
    unittest.main()
