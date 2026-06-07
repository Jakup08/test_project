from pathlib import Path
import os

root = Path(__file__).parent.resolve()
sorted_dir = root / 'sorted_media'
removed = 0
for p in sorted_dir.rglob('*'):
    if p.is_file():
        try:
            p.unlink()
            removed += 1
            print('Removed:', p)
        except Exception as e:
            print('Error removing', p, e)

print(f'Done. Removed {removed} files from sorted_media (folders kept).')
