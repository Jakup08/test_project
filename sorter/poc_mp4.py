#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="PoC: przenieś .mp4 do katalogu multimedialne")
    parser.add_argument("--src", default="sample_files", help="katalog źródłowy z plikami")
    args = parser.parse_args()

    src = Path(args.src).resolve()
    if not src.exists() or not src.is_dir():
        print(f"Katalog źródłowy nie istnieje: {src}")
        return

    dest = src.parent / "multimedialne"
    dest.mkdir(parents=True, exist_ok=True)

    moved = 0
    for f in src.iterdir():
        if f.is_file() and f.suffix.lower() == ".mp4":
            shutil.move(str(f), str(dest / f.name))
            print(f"Przeniesiono: {f.name} -> {dest}")
            moved += 1

    print(f"Gotowe. Przeniesiono {moved} plik(ów) .mp4")

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="PoC: przenieś .mp4 do katalogu multimedialne")
    parser.add_argument("--src", default="sample_files", help="katalog źródłowy z plikami")
    args = parser.parse_args()

    src = Path(args.src).resolve()
    if not src.exists() or not src.is_dir():
        print(f"Katalog źródłowy nie istnieje: {src}")
        return

    dest = src.parent / "multimedialne"
    dest.mkdir(parents=True, exist_ok=True)

    moved = 0
    for f in src.iterdir():
        if f.is_file() and f.suffix.lower() == ".mp4":
            shutil.move(str(f), str(dest / f.name))
            print(f"Przeniesiono: {f.name} -> {dest}")
            moved += 1

    print(f"Gotowe. Przeniesiono {moved} plik(ów) .mp4")

if __name__ == "__main__":
    main()
