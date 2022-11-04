from app.Konto import Konto


class KontoFirmowe(Konto):
    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        self.saldo = 0
        self.nip = ""
        self.sprawdz_nip(nip)
        self.historia = []

    def sprawdz_nip(self, nip):
        if len(nip) == 10:
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"
