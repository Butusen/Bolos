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






if __name__ == '__main__':
    unittest.main()
