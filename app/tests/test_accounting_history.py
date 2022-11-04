import unittest
from app.KontoFirmowe import KontoFirmowe
from app.Konto import Konto


class TestAccountingHistory(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "12345678912"
    nazwa = "Zakład Pogrzebowy A.S. Bytom"
    nip = "6262188083"

    def test_historii_ksiegowania(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(2000)
        konto.zaksieguj_przelew_przychodzacy(1000)
        konto.zaksieguj_przelew_wychodzacy(2000)
        self.assertEqual(konto.historia, [2000, 1000, -2000], "Zła historia dla przelewów zwykłych")

    def test_historii_ksiegowania_firma(self):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.zaksieguj_przelew_przychodzacy(2000)
        konto.zaksieguj_przelew_przychodzacy(1000)
        konto.zaksieguj_przelew_wychodzacy(2000)
        self.assertEqual(konto.historia, [2000, 1000, -2000], "Zla historia dla przelewów zwykłych w firmie")

    def test_historii_ksiegowania_ekspresowe(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.zaksieguj_przelew_przychodzacy(2000)
        konto.zaksieguj_przelew_przychodzacy(1000)
        konto.zaksieguj_przelew_wychodzacy(2000)
        konto.przelew_ekspresowy(300)
        self.assertEqual(konto.historia, [2000, 1000, -2000, -300, -1], "Zła historia dla przelewów ekspresowych")

    def test_historii_ksiegowania_ekspresowe_firma(self):
        konto = KontoFirmowe(self.nazwa, self.nip)
        konto.zaksieguj_przelew_przychodzacy(2000)
        konto.zaksieguj_przelew_przychodzacy(1000)
        konto.zaksieguj_przelew_wychodzacy(2000)
        konto.przelew_ekspresowy(300)
        self.assertEqual(konto.historia, [2000, 1000, -2000, -300, -5], "Zła historia dla przelewów ekspresowych w firmie")
