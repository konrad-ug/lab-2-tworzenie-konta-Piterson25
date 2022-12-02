import unittest
import requests


# odpalanie flaska
# export FLASK_APP=api/api.py
# python3 -m flask run
# odpalanie testu
# python3 -m unittest api_test/tests_obsluga_kont.py

class TestObslugaKont(unittest.TestCase):
    body = {
        "imie": "nick",
        "nazwisko": "cave",
        "pesel": "01292909876"
    }

    body2 = {
        "imie": "bob",
        "nazwisko": "marley"
    }

    url = "http://localhost:5000"

    def test_1_tworzenie_kont_poprawne(self):
        create_resp = requests.post(self.url + "/konta/stworz_konto", json=self.body)
        self.assertEqual(create_resp.status_code, 201)

    def test_2_get_po_peselu(self):
        get_resp = requests.get(self.url + f"/konta/konto/{self.body['pesel']}")
        self.assertEqual(get_resp.status_code, 200)
        resp_body = get_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body["imie"])
        self.assertEqual(resp_body["saldo"], 0)

    def test_3_put_po_peselu(self):
        put_resp = requests.put(self.url + f"/konta/update/{self.body['pesel']}", json=self.body2)
        self.assertEqual(put_resp.status_code, 200)
        resp_body = put_resp.json()
        self.assertEqual(resp_body["nazwisko"], self.body2["nazwisko"])
        self.assertEqual(resp_body["imie"], self.body2["imie"])

    def test_4_delete_po_peselu(self):
        delete_resp = requests.delete(self.url + f"/konta/delete/{self.body['pesel']}")
        self.assertEqual(delete_resp.status_code, 201)
