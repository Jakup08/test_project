#!/usr/bin/env python3
"""
Media File Sorter - Główny skrypt sortowania multimediów
Scalenie wszystkich PoC
"""
import argparse
import shutil
from pathlib import Path
from typing import Dict, List
import os

CATEGORIES = {
    "video": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".dav", ".webm", ".m4v", ".wmv", ".3gp", ".m3u8"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg", ".wma", ".opus", ".alac", ".aiff"],
    "obrazy": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".heic", ".raw", ".svg", ".ico", ".psd"],
    "dokumenty": [".pdf", ".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".txt", ".odt", ".rtf", ".csv", ".json", ".xml"],
    "archiwum": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".iso", ".dmg"],
    "kod": [".py", ".js", ".ts", ".java", ".cpp", ".c", ".h", ".html", ".css", ".php", ".go", ".rs", ".rb", ".sh"],
}

EXT_TO_CATEGORY = {}
for category, exts in CATEGORIES.items():
    for ext in exts:
        EXT_TO_CATEGORY[ext.lower()] = category

DEFAULT_EXTS = list(EXT_TO_CATEGORY.keys())


def format_size(bytes_size: int) -> str:
    """Format bajty do czytelnego formatu"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"


def sort_files(src: Path, dest: Path, exts: List[str], recursive: bool = False) -> Dict:
    """Sortuj pliki do kategorii i zwróć statystyki"""
    stats = {"total_moved": 0, "total_size": 0, "by_category": {}, "errors": []}

    exts_normalized = [e.lower() if e.startswith('.') else f'.{e.lower()}' for e in exts]
    pattern = "**/*" if recursive else "*"
    files = list(src.glob(pattern))

    print(f"Znaleziono {len(files)} plik(ów), sortowanie...\n")

    for f in files:
        if not f.is_file():
            continue

        suffix = f.suffix.lower()
        if suffix not in exts_normalized:
            continue

        try:
            file_size = f.stat().st_size
            category = EXT_TO_CATEGORY.get(suffix, "inne")
            category_dest = dest / category
            category_dest.mkdir(parents=True, exist_ok=True)

            new_path = category_dest / f.name
            if new_path.exists():
                base = f.stem
                ext = f.suffix
                counter = 1
                while new_path.exists():
                    new_name = f"{base}_{counter}{ext}"
                    new_path = category_dest / new_name
                    counter += 1

            try:
                if f.resolve() == new_path.resolve():
                    continue
            except Exception:
                pass

            shutil.move(str(f), str(new_path))

            stats["total_moved"] += 1
            stats["total_size"] += file_size
            if category not in stats["by_category"]:
                stats["by_category"][category] = {"count": 0, "size": 0}
            stats["by_category"][category]["count"] += 1
            stats["by_category"][category]["size"] += file_size

            print(f"  ✓ {f.name} ({format_size(file_size)}) → {category}/")

        except Exception as e:
            stats["errors"].append(str(e))
            print(f"  ✗ {f.name} - Błąd: {e}")

    return stats


def print_summary(stats: Dict):
    """Wydrukuj podsumowanie sortowania"""
    print("\n" + "="*70)
    print("PODSUMOWANIE SORTOWANIA")
    print("="*70)
    print(f"Przeniesiono: {stats['total_moved']} plik(ów)")
    print(f"Całkowity rozmiar: {format_size(stats['total_size'])}")

    if stats["by_category"]:
        print("\nStatystyki po kategorii:")
        for category, data in sorted(stats["by_category"].items()):
            count_str = f"{data['count']:3}"
            size_str = format_size(data['size']).rjust(12)
            print(f"  {category:15} → {count_str} plik(ów) | {size_str}")

    if stats["errors"]:
        print(f"\nBłędy ({len(stats['errors'])}):")
        for err in stats["errors"][:5]:
            print(f"  - {err}")
        if len(stats["errors"]) > 5:
            print(f"  ... i {len(stats['errors']) - 5} więcej")


def create_test_files(dest: Path = Path("sample_files")):
    """Utwórz przykładowe pliki z wielu kategorii do testowania"""
    dest.mkdir(exist_ok=True)

    test_files = {
        "film1.mp4": 1024 * 100,
        "film2.mkv": 1024 * 500,
        "recording.dav": 1024 * 1024,
        "video.avi": 1024 * 300,
        "piosenka.mp3": 1024 * 200,
        "muzyka.wav": 1024 * 1024 * 5,
        "audio.aac": 1024 * 150,
        "track.flac": 1024 * 1024 * 3,
        "foto1.jpg": 1024 * 50,
        "zdjecie.png": 1024 * 80,
        "screenshot.heic": 1024 * 60,
        "obraz.gif": 1024 * 100,
        "ikona.webp": 1024 * 30,
        "raport.pdf": 1024 * 200,
        "dokument.docx": 1024 * 150,
        "arkusz.xlsx": 1024 * 120,
        "prezentacja.pptx": 1024 * 300,
        "notatka.txt": 1024 * 10,
        "pliki.zip": 1024 * 1024 * 2,
        "backup.rar": 1024 * 1024 * 3,
        "archiwum.7z": 1024 * 1024,
        "skrypt.py": 1024 * 50,
        "aplikacja.js": 1024 * 80,
        "strona.html": 1024 * 40,
        "style.css": 1024 * 30,
    }

    print("Tworzę pliki testowe...\n")
    for filename, size in test_files.items():
        filepath = dest / filename
        if not filepath.exists():
            with open(filepath, 'wb') as f:
                f.write(os.urandom(size))
            print(f"  ✓ {filename} ({size // 1024} KB)")
        else:
            print(f"  ⊘ {filename} (już istnieje)")

    print(f"\nUtworzono/znaleziono pliki w: {dest}\n")


def list_extensions():
    """Wyświetl dostępne kategorie i rozszerzenia"""
    print("\nDOSTĘPNE KATEGORIE I ROZSZERZENIA\n")
    for category, exts in sorted(CATEGORIES.items()):
        print(f"{category.upper()}:")
        ext_str = "  " + ", ".join(sorted(exts))
        print(f"{ext_str}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Media File Sorter - Sortuj multimedialne pliki do katalogów",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
PRZYKŁADY:
  1. Sortuj z domyślnymi ustawieniami:
     python sorter.py

  2. Własne katalogi:
     python sorter.py --src ~/Videos --dest ~/sorted_media

  3. Rekurencyjne (podkatalogi):
     python sorter.py --recursive

  4. Tylko określone rozszerzenia:
     python sorter.py --exts mp4 mkv wav mp3

  5. Utwórz pliki testowe:
     python sorter.py --test-create

  6. Wyświetl dostępne typy:
     python sorter.py --list-types
        """
    )

    parser.add_argument("--src", default="sample_files", help="katalog źródłowy (default: sample_files)")
    parser.add_argument("--dest", default="sorted_media", help="katalog docelowy (default: sorted_media)")
    parser.add_argument("--exts", nargs="*", default=DEFAULT_EXTS, help="lista rozszerzeń do sortowania")
    parser.add_argument("--recursive", action="store_true", help="przeszukuj rekurencyjnie podkatalogi")
    parser.add_argument("--test-create", action="store_true", help="utwórz pliki testowe")
    parser.add_argument("--list-types", action="store_true", help="wyświetl dostępne typy plików")

    args = parser.parse_args()

    if args.list_types:
        list_extensions()
        return

    if args.test_create:
        create_test_files(Path(args.src))
        return

    src = Path(args.src).resolve()
    if not src.exists() or not src.is_dir():
        print(f"Katalog nie istnieje: {src}")
        return

    dest_arg = Path(args.dest)
    if dest_arg.is_absolute():
        dest = dest_arg
    else:
        dest = src.parent / dest_arg
    dest = dest.resolve()

    try:
        dest.relative_to(src)
        print(f"Błąd: katalog docelowy nie może być podkatalogiem źródła: {dest}")
        return
    except ValueError:
        pass

    dest.mkdir(parents=True, exist_ok=True)

    print(f"Źródło: {src}\nCel: {dest}\nRekurencyjnie: {'Tak' if args.recursive else 'Nie'}\nTypy: {len(args.exts)} rozszerzeń")

    stats = sort_files(src, dest, args.exts, args.recursive)
    print_summary(stats)


if __name__ == "__main__":
    main()
