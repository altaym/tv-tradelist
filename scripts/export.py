from pathlib import Path
from datetime import datetime


class Export:

    def __init__(self, folder="data"):

        self.folder = Path(folder)

        self.folder.mkdir(parents=True, exist_ok=True)

    def save(self, filename, symbols, title=None):

        file = self.folder / filename

        symbols = sorted(set(symbols))

        with open(file, "w", encoding="utf-8") as f:

            if title:
                f.write(f"# {title}\n")

            f.write(f"# Generated : {datetime.now():%Y-%m-%d %H:%M:%S}\n")
            f.write(f"# Count : {len(symbols)}\n\n")

            for s in symbols:
                f.write(f"BIST:{s}\n")

        print(f"✔ {filename} ({len(symbols)})")

    def report(self, stats):

        file = self.folder / "Rapor.txt"

        with open(file, "w", encoding="utf-8") as f:

            f.write("TradingView WatchLists\n")
            f.write("=" * 40 + "\n\n")

            f.write(f"Oluşturma : {datetime.now():%d.%m.%Y %H:%M:%S}\n\n")

            for key, value in stats.items():
                f.write(f"{key:<30}: {value}\n")

        print("✔ Rapor.txt")