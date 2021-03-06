from unittest import TestCase
from TDD.src.leilao.dominio import Usuario, Lance, Leilao
from TDD.src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.lance_do_gui = Lance(self.gui, 100.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_menor_e_o_maior_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 150.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 500.0)
            self.leilao.propoe(lance_do_yuri)
            self.leilao.propoe(self.lance_do_gui)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(100.0, self.leilao.maior_lance)
        self.assertEqual(100.0, self.leilao.menor_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_3_lances(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 150.0)
        vini = Usuario('Vini', 500.0)
        lance_do_vini = Lance(vini, 200.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_vini)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe((self.lance_do_gui))
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)

    def test_deve_permitir_propor_um_lance_caso_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 150.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebido)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        outro_lance_do_gui = Lance(self.gui, 200.0)
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(outro_lance_do_gui)


