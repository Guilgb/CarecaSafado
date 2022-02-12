from unittest import TestCase
import unittest
from dominio import Usuario, Lance, Leilao, Avaliador


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

        self.leilao.lances.append(self.lance_camy)
        self.leilao.lances.append(self.lance_gui)
        self.leilao.lances.append(self.lance_gael)
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 20
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)

        maior_valor_esperado = 200
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def teste_avalia2(self):
        self.leilao.lances.append(self.lance_gael)
        self.leilao.lances.append(self.lance_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 20
        maior_valor_esperado = 100

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)


if __name__ == '__main__':
    unittest.main()
