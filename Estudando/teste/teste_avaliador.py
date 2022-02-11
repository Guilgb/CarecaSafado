from unittest import TestCase
import unittest
from dominio import Usuario, Lance, Leilao, Avaliador


class TesteAvaliador(TestCase):
    def test_avalia(self):
        gui = Usuario("Guilherme")
        camyla = Usuario("Camyla")
        # gael = Usuario("Gael")

        lance_gui = Lance(gui, 100)
        lance_camy = Lance(camyla, 200)
        # lance_gael = Lance(gael, 20)

        leilao = Leilao("Lance de Celulares")
        leilao.lances.append(lance_camy)
        leilao.lances.append(lance_gui)
        # leilao.lances.append(lance_gael)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100
        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)

        maior_valor_esperado = 200
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    if __name__ == '__main__':
        unittest.main()
