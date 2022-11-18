import unittest
from ..Konto import Konto
from ..KontoFirmowe import KontoFirmowe
from parameterized import parameterized


class TestTakingLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "72345678912"
    nazwa = "Zakład Pogrzebowy A.S. Bytom"
    nip = "6262188083"

    def setUp(self):
        self.konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.kontoFirmowe = KontoFirmowe(self.nazwa, self.nip)

    @parameterized.expand([
        ([-100, 100, 100, 100, 600], 500, True, 500),
        ([-100, 100, 0, 100, 600], 500, True, 500),
        ([-100000, 100, 100, 100, 600], 500, False, 0),
        ([], 1000, False, 0)
    ])
    def test_zaciaganie_kredytu(self, historia, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.konto.historia = historia
        czy_przyznany = self.konto.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

    @parameterized.expand([
        ([-1775, 2000, 50000], 52000, 10000, True, 62000),
        ([-1775, 4000], 4000, 2000, True, 6000),
        ([1000, 500], 1500, 500, False, 1500),
        ([-1775, 2000], 2000, 1700, False, 2000),
        ([], 500, 100, False, 500)
    ])
    def test_kredyt_firmowy(self, historia, saldo, kwota, oczekiwany_wynik, oczekiwane_saldo):
        self.kontoFirmowe.historia = historia
        self.kontoFirmowe.saldo = saldo
        czy_przyznany = self.kontoFirmowe.zaciagnij_kredyt(kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik)
        self.assertEqual(self.kontoFirmowe.saldo, oczekiwane_saldo)
