import pandas as pd
import requests
from io import StringIO


class VBTS:

    URL = "https://www.borsaistanbul.com/erd/menkul_tedbir_listesi.csv"

    def __init__(self):
        self.df = None

    def load(self):

        r = requests.get(self.URL, timeout=30)
        r.raise_for_status()

        self.df = pd.read_csv(
            StringIO(r.text),
            sep=";"
        )

        self.df.columns = [c.strip() for c in self.df.columns]

    def _find_column(self, words):

        for c in self.df.columns:

            cc = c.lower()

            if all(w in cc for w in words):
                return c

        return None

    @property
    def symbol_column(self):

        for c in self.df.columns:

            cc = c.lower()

            if "kod" in cc:
                return c

            if "işlem" in cc:
                return c

        raise Exception("Kod kolonu bulunamadı")

    @property
    def tedbir_column(self):

        for c in self.df.columns:

            if "tedbir" in c.lower():
                return c

        raise Exception("Tedbir kolonu bulunamadı")

    def filter(self, text):

        x = self.df[
            self.df[self.tedbir_column]
            .astype(str)
            .str.contains(text,
                          case=False,
                          na=False)
        ]

        return set(
            x[self.symbol_column]
            .astype(str)
            .str.strip()
        )

    def brut(self):
        return self.filter("Brüt")

    def kredi(self):
        return self.filter("Kredili")

    def aciga(self):
        return self.filter("Açığa")

    def emir(self):
        return self.filter("Emir")

    def tek_fiyat(self):
        return self.filter("Tek Fiyat")

    def internet(self):
        return self.filter("İnternet")

    def depo(self):
        return self.filter("Depo")

    def all(self):

        return set(
            self.df[self.symbol_column]
        )