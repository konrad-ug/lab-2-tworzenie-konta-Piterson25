from app.Konto import Konto
from datetime import date
import requests
import os


class KontoFirmowe(Konto):
    def __init__(self, nazwa, nip):
        self.nazwa = nazwa
        self.saldo = 0
        self.nip = ""
        self.sprawdz_nip(nip)
        self.historia = []

    def sprawdz_nip(self, nip):
        if len(nip) == 10:
            if self.czy_nip_istnieje(nip) is None:
                self.nip = "Pranie!"
            else:
                self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"

    def czy_nip_istnieje(self, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        url = f"{gov_url}api/search/nip/{nip}?date={date.today()}"
        get_resp = requests.get(url)
        resp_body = get_resp.json()
        return resp_body['result']['subject']

    def zaciagnij_kredyt(self, kwota):
        if -1775 in self.historia and self.saldo >= kwota * 2:
            self.zaksieguj_przelew_przychodzacy(kwota)
            return True
        return False
