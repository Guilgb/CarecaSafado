from unittest import TestCase
import unittest
from dominio import Usuario, Lance, Leilao


class TesteAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario("Guilherme")
        self.camyla = Usuario("Camyla")
        self.gael = Usuario("Gael")

        self.lance_gui = Lance(self.gui, 100)
        self.lance_camy = Lance(self.camyla, 200)
        self.lance_gael = Lance(self.gael, 20)

        self.leilao = Leilao("Lance de Celulares")

    def test_avalia(self):

        self.leilao.propoe(self.lance_camy)
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(self.lance_gael)

        menor_valor_esperado = 20
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)

        maior_valor_esperado = 200
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def teste_avalia2(self):
        self.leilao.propoe(self.lance_gael)
        self.leilao.propoe(self.lance_gui)

        menor_valor_esperado = 20
        maior_valor_esperado = 100

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


if __name__ == '__main__':
    unittest.main()
