class Konto:
    def __init__(self, imie, nazwisko, pesel, kod_rabatowy=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = 0
        self.pesel = ""
        self.historia = []

        self.sprawdz_pesel(pesel)
        self.sprawdz_kod(kod_rabatowy)

    def sprawdz_pesel(self, pesel):
        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel!"

    def sprawdz_kod(self, kod_rabatowy):
        if kod_rabatowy:
            if len(kod_rabatowy) == 8 and kod_rabatowy[:5] == "PROM_" and int(self.pesel[:2]) > 60 and int(
                    self.pesel[2:4]) > 20:
                self.saldo = 50
            else:
                self.saldo = 0

    def zaksieguj_przelew_wychodzacy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.historia.append(-kwota)

    def zaksieguj_przelew_przychodzacy(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def przelew_ekspresowy(self, kwota):
        try:
            self.nazwa
            oplata = 5
        except:
            oplata = 1

        if self.saldo - kwota - oplata >= -oplata:
            self.saldo -= kwota + oplata
            self.historia.append(-kwota)
            self.historia.append(-oplata)
