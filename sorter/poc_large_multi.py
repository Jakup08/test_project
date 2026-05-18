#!/usr/bin/env python3
"""
PoC: Sortuj wiele plików z różnymi rozszerzeniami (także duże pliki)
"""
import argparse
import shutil
from pathlib import Path
from typing import Dict, List
import os

# Wspólne rozszerzenia multimedialne (także rzadkie)
DEFAULT_EXTS = [
    ".mp4", ".dav", ".heic", ".mkv", ".avi", ".mov", ".flv",
    ".mp3", ".wav", ".aac", ".flac", ".m4a",
    ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff"
]

def format_size(bytes_size: int) -> str:
    """Format bytes do czytelnego formatu"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024.0:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024.0
    return f"{bytes_size:.2f} PB"

def process_files(src: Path, dest: Path, exts: List[str], recursive: bool = False) -> Dict:
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
    
    print(f"Znaleziono {len(files)} plik(ów), sortowanie...")
    
    for f in files:
        if not f.is_file():
            continue
        
        suffix = f.suffix.lower()
        if suffix not in exts_normalized:
            continue
        
        try:
            file_size = f.stat().st_size
            
            # Utwórz podkatalog dla rozszerzenia
            ext_dest = dest / suffix[1:].upper()  # Usuń punkt i zamień na UPPER
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
            
            print(f"✓ {f.name} ({format_size(file_size)}) -> {ext_dest.name}/")
            
        except Exception as e:
            stats["errors"].append(str(e))
            print(f"✗ Błąd: {f.name} - {e}")
    
    return stats

def print_summary(stats: Dict):
    """Wydrukuj podsumowanie"""
    print("\n" + "="*60)
    print("PODSUMOWANIE")
    print("="*60)
    print(f"Przeniesiono: {stats['total_moved']} plik(ów)")
    print(f"Całkowity rozmiar: {format_size(stats['total_size'])}")
    
    if stats["by_extension"]:
        print("\nStatystyki po rozszerzeniu:")
        for ext, data in sorted(stats["by_extension"].items()):
            print(f"  {ext:10} - {data['count']:3} plik(ów), {format_size(data['size']):>12}")
    
    if stats["errors"]:
        print(f"\nBłędy ({len(stats['errors'])}):")
        for err in stats["errors"][:5]:
            print(f"  - {err}")
        if len(stats["errors"]) > 5:
            print(f"  ... i {len(stats['errors']) - 5} więcej")

def main():
    parser = argparse.ArgumentParser(
        description="PoC: Sortuj wiele plików do oddzielnych katalogów po rozszerzeniu"
    )
    parser.add_argument("--src", default="sample_files", help="katalog źródłowy")
    parser.add_argument("--dest", default="multimedialne", help="katalog docelowy")
    parser.add_argument("--exts", nargs="*", default=DEFAULT_EXTS, 
                       help="lista rozszerzeń do sortowania")
    parser.add_argument("--recursive", action="store_true", 
                       help="przeszukuj rekurencyjnie podkatalogi")
    parser.add_argument("--list-exts", action="store_true", 
                       help="wyświetl domyślne rozszerzenia")
    
    args = parser.parse_args()
    
    if args.list_exts:
        print("Domyślne rozszerzenia:")
        for ext in sorted(set([e.split('.')[-1] for e in DEFAULT_EXTS])):
            print(f"  - .{ext}")
        return
    
    src = Path(args.src).resolve()
    if not src.exists() or not src.is_dir():
        print(f"✗ Katalog nie istnieje: {src}")
        return
    
    dest = src.parent / args.dest
    dest.mkdir(parents=True, exist_ok=True)
    
    print(f"Źródło: {src}")
    print(f"Cel: {dest}")
    print(f"Rekurencyjnie: {args.recursive}")
    print(f"Szukane rozszerzenia: {len(args.exts)}")
    print()
    
    stats = process_files(src, dest, args.exts, args.recursive)
    print_summary(stats)

if __name__ == "__main__":
    main()
