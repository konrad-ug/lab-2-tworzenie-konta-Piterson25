import unittest
from ..Konto import Konto


class TestTakingLoan(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "72345678912"

    def test_3_przychodzace_przelewy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, 100, 100, 600]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertEqual(czy_przyznany, True, "Nie zaciagnieto kredytu")
        self.assertEqual(konto.saldo, 500, "Srodki sie nie zgadzaja")

    def test_3_przychodzace_przelewy_nie_wplaty(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, 100, -100, 600]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertEqual(czy_przyznany, False, "Przyznano kredyt gdzie ostatnie 3 transakcje nie byly wplatami")
        self.assertEqual(konto.saldo, 0, "Srodki zostaly powiekszone a nie powinny")

    def test_5_przychodzace_przelewy(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, 100, 1, 100, 600]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertEqual(czy_przyznany, True, "Nie zaciagnieto kredytu")
        self.assertEqual(konto.saldo, 500, "Srodki sie nie zgadzaja")

    def test_5_ostatnich_transakcji_za_mala_suma(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-700, -500, 100, 100, 200]
        czy_przyznany = konto.zaciagnij_kredyt(500)
        self.assertEqual(czy_przyznany, False, "Suma ostatnich 5 transakcji jest mniejsza od kredytu")
        self.assertEqual(konto.saldo, 0, "Srodki zostaly powiekszone a nie powinny")

    def test_3_i_5_ostatnich_transakcji_zle(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel)
        konto.historia = [-100, -100, -100, -100, -200]
        czy_przyznany = konto.zaciagnij_kredyt(10000)
        self.assertEqual(czy_przyznany, False, "Suma ostatnich 5 transakcji jest mniejsza od kredytu i ostatnie 3"
                                               "transakcje nie byly wplatami")
        self.assertEqual(konto.saldo, 0, "Srodki zostaly powiekszone a nie powinny")
