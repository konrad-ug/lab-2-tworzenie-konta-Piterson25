from app.Konto import Konto


class RejestrKont():
    konta = []

    @classmethod
    def add_account(cls, Konto):
        cls.konta.append(Konto)

    @classmethod
    def find_account(cls, pesel):
        for k in cls.konta:
            if k.pesel == pesel:
                return k
        return None

    @classmethod
    def accounts(cls):
        return len(cls.konta)
