#!/usr/bin/env python3
"""
Media File Sorter - Główny skrypt sortowania multimediów
Scalenie wszystkich PoC: poc_mp4.py, poc_multi.py, poc_large_multi.py
"""
import argparse
import shutil
from pathlib import Path
from typing import Dict, List
import os

# Wszystkie wspólne rozszerzenia multimedialne
EXTENSIONS = {
    "video": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".dav", ".webm", ".m4v"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg", ".wma", ".opus"],
    "photo": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".heic", ".raw"],
}

DEFAULT_EXTS = [ext for exts in EXTENSIONS.values() for ext in exts]


def format_size(bytes_size: int) -> str:
    """Format bajty do czytelnego formatu"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"


def sort_files(src: Path, dest: Path, exts: List[str], recursive: bool = False) -> Dict:
    """Sortuj pliki i zwróć statystyki"""
    stats = {
        "total_moved": 0,
        "total_size": 0,
        "by_extension": {},
        "errors": []
    }

    # Przygotuj rozszerzenia
    exts_normalized = [e.lower() if e.startswith('.') else f'.{e.lower()}' for e in exts]
    
    # Przeszukaj pliki
    pattern = "**/*" if recursive else "*"
    files = list(src.glob(pattern))
    
    print(f"🔍 Znaleziono {len(files)} plik(ów), sortowanie...\n")
    
    for f in files:
        if not f.is_file():
            continue
        
        suffix = f.suffix.lower()
        if suffix not in exts_normalized:
            continue
        
        try:
            file_size = f.stat().st_size
            
            # Utwórz podkatalog dla rozszerzenia (UPPER bez punktu)
            ext_dest = dest / suffix[1:].upper()
            ext_dest.mkdir(parents=True, exist_ok=True)
            
            # Przenieś plik
            new_path = ext_dest / f.name
            shutil.move(str(f), str(new_path))
            
            # Zaktualizuj statystyki
            stats["total_moved"] += 1
            stats["total_size"] += file_size
            if suffix not in stats["by_extension"]:
                stats["by_extension"][suffix] = {"count": 0, "size": 0}
            stats["by_extension"][suffix]["count"] += 1
            stats["by_extension"][suffix]["size"] += file_size
            
            print(f"  ✓ {f.name} ({format_size(file_size)}) → {ext_dest.name}/")
            
        except Exception as e:
            stats["errors"].append(str(e))
            print(f"  ✗ {f.name} - Błąd: {e}")
    
    return stats


def print_summary(stats: Dict):
    """Wydrukuj podsumowanie sortowania"""
    print("\n" + "="*70)
    print("📊 PODSUMOWANIE SORTOWANIA")
    print("="*70)
    print(f"✓ Przeniesiono: {stats['total_moved']} plik(ów)")
    print(f"💾 Całkowity rozmiar: {format_size(stats['total_size'])}")
    
    if stats["by_extension"]:
        print("\n📂 Statystyki po rozszerzeniu:")
        for ext, data in sorted(stats["by_extension"].items()):
            count_str = f"{data['count']:3}"
            size_str = format_size(data['size']).rjust(12)
            print(f"  {ext:10} → {count_str} plik(ów) | {size_str}")
    
    if stats["errors"]:
        print(f"\n⚠️  Błędy ({len(stats['errors'])}):")
        for err in stats["errors"][:5]:
            print(f"  - {err}")
        if len(stats["errors"]) > 5:
            print(f"  ... i {len(stats['errors']) - 5} więcej")


def create_test_files(dest: Path = Path("sample_files")):
    """Utwórz przykładowe pliki multimedialne do testowania"""
    dest.mkdir(exist_ok=True)
    
    test_files = {
        "video1.mp4": 1024 * 100,           # 100 KB
        "video2.mkv": 1024 * 500,           # 500 KB
        "recording.dav": 1024 * 1024,       # 1 MB
        "photo1.jpg": 1024 * 50,            # 50 KB
        "photo2.png": 1024 * 80,            # 80 KB
        "screenshot.heic": 1024 * 60,       # 60 KB
        "audio.mp3": 1024 * 200,            # 200 KB
        "music.wav": 1024 * 1024 * 5,       # 5 MB
    }
    
    print("📝 Tworzę pliki testowe...\n")
    for filename, size in test_files.items():
        filepath = dest / filename
        if not filepath.exists():  # Nie nadpisuj istniejących
            with open(filepath, 'wb') as f:
                f.write(os.urandom(size))
            print(f"  ✓ {filename} ({size // 1024} KB)")
        else:
            print(f"  ⊘ {filename} (już istnieje)")
    
    print(f"\n✓ Utworzono/znaleziono pliki w: {dest}\n")


def list_extensions():
    """Wyświetl dostępne typy plików"""
    print("\n📋 DOSTĘPNE TYPY PLIKÓW\n")
    for category, exts in EXTENSIONS.items():
        print(f"🎬 {category.upper()}:")
        ext_str = "  " + ", ".join(sorted(exts))
        print(f"{ext_str}\n")


def main():
    parser = argparse.ArgumentParser(
        description="🎬 Media File Sorter - Sortuj multimedialne pliki do katalogów",
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
    
    parser.add_argument("--src", default="sample_files", 
                       help="katalog źródłowy (default: sample_files)")
    parser.add_argument("--dest", default="multimedialne", 
                       help="katalog docelowy (default: multimedialne)")
    parser.add_argument("--exts", nargs="*", default=DEFAULT_EXTS,
                       help="lista rozszerzeń do sortowania")
    parser.add_argument("--recursive", action="store_true",
                       help="przeszukuj rekurencyjnie podkatalogi")
    parser.add_argument("--test-create", action="store_true",
                       help="utwórz pliki testowe")
    parser.add_argument("--list-types", action="store_true",
                       help="wyświetl dostępne typy plików")
    
    args = parser.parse_args()
    
    # Opcje specjalne
    if args.list_types:
        list_extensions()
        return
    
    if args.test_create:
        create_test_files(Path(args.src))
        return
    
    # Główny proces sortowania
    src = Path(args.src).resolve()
    if not src.exists() or not src.is_dir():
        print(f"❌ Katalog nie istnieje: {src}")
        return
    
    dest = src.parent / args.dest
    dest.mkdir(parents=True, exist_ok=True)
    
    print(f"""
╔════════════════════════════════════════════════════════════════╗
║        🎬 MEDIA FILE SORTER - SORTOWANIE MULTIMEDIÓW          ║
╚════════════════════════════════════════════════════════════════╝

📁 Źródło:      {src}
📁 Cel:         {dest}
🔄 Rekurencyjnie: {"Tak ✓" if args.recursive else "Nie"}
🏷️  Typy:        {len(args.exts)} rozszerzeń
    """)
    
    stats = sort_files(src, dest, args.exts, args.recursive)
    print_summary(stats)


if __name__ == "__main__":
    main()
