# Piotr Maszczak grupa 2

Odpalanie Flaska
```
export FLASK_APP=app/api.py
python3 -m flask run
```
Odpalanie testu do Flaska
```
python3 -m unittest app/tests/test_obsluga_kont.py
```
Coverage i unittest
```
python -m coverage run -m unittest
python -m coverage report
python -m coverage html
```
```
export BANK_APP_MF_URL="https://wl-api.mf.gov.pl/api/search/nip/"
```
