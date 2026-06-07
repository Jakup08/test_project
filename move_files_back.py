from pathlib import Path
import shutil

ROOT = Path(__file__).parent.resolve()
SRC = ROOT / 'sorted_media'
DST = ROOT / 'sample_files'

moved = 0
errors = []

for p in SRC.rglob('*'):
    if p.is_file():
        try:
            rel = p.name
            dest_path = DST / rel
            # avoid overwriting
            if dest_path.exists():
                base = dest_path.stem
                ext = dest_path.suffix
                counter = 1
                while dest_path.exists():
                    dest_path = DST / f"{base}_{counter}{ext}"
                    counter += 1
            shutil.move(str(p), str(dest_path))
            moved += 1
            print(f"Moved: {p} -> {dest_path}")
        except Exception as e:
            errors.append((str(p), str(e)))

print(f"\nDone. Moved {moved} files.")
if errors:
    print('Errors:')
    for e in errors:
        print(e)
