
#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

DEFAULT_EXTS = [".mp4", ".dav", ".heic"]

def main():
	parser = argparse.ArgumentParser(description="PoC: przenieś wiele rozszerzeń do katalogu multimedialne")
	parser.add_argument("--src", default="sample_files", help="katalog źródłowy z plikami")
	parser.add_argument("--exts", nargs="*", default=DEFAULT_EXTS, help="lista rozszerzeń do przeniesienia")
	args = parser.parse_args()

	src = Path(args.src).resolve()
	if not src.exists() or not src.is_dir():
		print(f"Katalog źródłowy nie istnieje: {src}")
		return

	dest = src.parent / "multimedialne"
	dest.mkdir(parents=True, exist_ok=True)

	exts = [e.lower() if e.startswith('.') else f'.{e.lower()}' for e in args.exts]
	moved = 0
	for f in src.iterdir():
		if f.is_file() and f.suffix.lower() in exts:
			shutil.move(str(f), str(dest / f.name))
			print(f"Przeniesiono: {f.name} -> {dest}")
			moved += 1

	print(f"Gotowe. Przeniesiono {moved} plik(ów): {', '.join(exts)}")

if __name__ == "__main__":
	main()

