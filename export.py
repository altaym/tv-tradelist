from pathlib import Path

class Export:

    def __init__(self):
        self.folder = Path("data")
        self.folder.mkdir(exist_ok=True)

    def txt(self,name,symbols):
        file=self.folder/name
        with open(file,"w",encoding="utf8") as f:
            for s in sorted(symbols):
                f.write(f"BIST:{s}\n")
