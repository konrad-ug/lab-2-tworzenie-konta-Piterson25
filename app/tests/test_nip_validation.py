import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe

class TestNipValidation(unittest.TestCase):
    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=True)
    def test_1_prawidlowy_nip(self):
        konto_firmowe = KontoFirmowe("Jakub", "42142149417")
        self.assertEqual(konto_firmowe.nip, "42142149417")

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje', return_value=None)
    def test_2_nieprawidlowy_nip(self):
        konto_firmowe = KontoFirmowe("Arek", "0000000000")
        self.assertEqual(konto_firmowe.nip, "Pranie!")
