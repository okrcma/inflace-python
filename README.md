# inflace-python

Calculates Czech inflation between two months (starting from 01/2018).

Scrapes and parses data from https://vdb.czso.cz/, specifically
https://vdb.czso.cz/vdbvo2/faces/cs/index.jsf?page=vystup-objekt&z=T&f=TABULKA&ds=ds2329&pvo=CEN083A&skupId=2218&katalog=31779&o=false&evo=v2504_%21_CEN-SPO-BAZIC2015-EM_1&str=v514.

## Install

1. Get Python 3.10
2. (Optional) Create virtual environment to not clutter your global one
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install requirements
   ```bash
   python3 -m pip install -r requirements.txt
   ```
4. Add sources to PYTHONPATH
   ```bash
   export PYTHONPATH=$(pwd):$PYTHONPATH
   ```

## Run

```bash
python3 inflace/main.py 01/2018 01/2024
```
