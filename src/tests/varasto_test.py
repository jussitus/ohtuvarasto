import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.varasto_neg = Varasto(-1, -1)
        self.varasto_yli = Varasto(10, 11)
    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_uudella_varastolla_ei_neg_tilavuus(self):
        self.assertAlmostEqual(self.varasto_neg.tilavuus, 0)

    def test_uudella_varastolla_ei_neg_saldo(self):
        self.assertAlmostEqual(self.varasto_neg.saldo, 0)

    def test_uudella_varastolla_saldo_enintaan_tilavuus(self):
        self.assertAlmostEqual(self.varasto_yli.saldo, self.varasto_yli.tilavuus)

    def test_lisays_neg_maaran_lisays_ei_muuta_saldoa(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo_ennen)

    def test_lisays_saldo_ei_ylita_tilavuutta(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus + 1)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)
    
    def test_ottaminen_neg_maaran_ottaminen_ei_muuta_saldoa(self):
        saldo_ennen = self.varasto.saldo
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo_ennen)
    
    def test_ottaminen_neg_maaran_ottaminen_palauttaa_nollan(self):
        otto = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(otto, 0)

    def test_ottaminen_yli_saldon_nollaa_saldon(self):
        self.varasto.ota_varastosta(self.varasto.saldo + 1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ottaminen_yli_saldon_ottaminen_palauttaa_saldon(self):
        saldo_ennen = self.varasto.saldo
        otto = self.varasto.ota_varastosta(self.varasto.saldo + 1)
        self.assertAlmostEqual(otto, saldo_ennen)

    def test_str_metodi_palauttaa_oikean_merkkijonon(self):
        merkkijono = str(self.varasto)
        self.assertEqual(merkkijono, f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")