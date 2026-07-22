import requests
import pandas as pd
from bs4 import BeautifulSoup

class BIST:

    def __init__(self):
        self.url = "https://www.kap.org.tr/tr/bist-sirketler"

    def get_symbols(self):
        print("BIST şirketleri okunuyor...")
        html = requests.get(self.url, timeout=30).text
        soup = BeautifulSoup(html, "lxml")
        table = soup.find("table")
        rows = table.find_all("tr")
        symbols = []

        for row in rows[1:]:
            cols = row.find_all("td")

            if len(cols) < 2:
                continue

            code = cols[0].text.strip().upper()

            if code:
                symbols.append(code)

        return sorted(list(set(symbols)))
