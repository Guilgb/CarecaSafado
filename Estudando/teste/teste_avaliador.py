from unittest import TestCase
import unittest
from dominio import Usuario, Lance, Leilao


class TesteLeilao(TestCase):

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

    # se o leilao n tiver lance, permite propor um lance
    def test_npermite(self):
        self.leilao.propoe(self.lance_gui)

        quantidades_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidades_de_lances)

    # se o usuario for diferente propoe o lance
    def test_permite(self):
        mary = Usuario("Mary")
        lance_mary = Lance(mary, 212)
        self.leilao.propoe(lance_mary)
        self.leilao.propoe(self.lance_gui)

        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances)
    # não permite o lance se o usuario for o mesmo

    def mesmo_lance(self):
        lance_do_gui = (self.gui, 220)

        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(self.lance_gui)

        quantidade_de_lances_recebidos = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebidos)


if __name__ == '__main__':
    unittest.main()
