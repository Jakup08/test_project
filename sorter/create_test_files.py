#!/usr/bin/env python3
"""
Test: Utwórz przykładowe pliki do testowania sortowania
"""
import os
from pathlib import Path

def create_test_files():
    """Utwórz przykładowe pliki różnych typów i rozmiarów"""
    sample_dir = Path("sample_files")
    sample_dir.mkdir(exist_ok=True)
    
    # Pliki testowe o różnych rozmiarach
    test_files = {
        "video1.mp4": 1024 * 100,      # 100 KB
        "video2.mkv": 1024 * 500,      # 500 KB
        "recording.dav": 1024 * 1024,  # 1 MB
        "photo1.jpg": 1024 * 50,       # 50 KB
        "photo2.png": 1024 * 80,       # 80 KB
        "screenshot.heic": 1024 * 60,  # 60 KB
        "audio.mp3": 1024 * 200,       # 200 KB
        "music.wav": 1024 * 1024 * 5,  # 5 MB
        "document.pdf": 1024 * 300,    # 300 KB (nie będzie sortowany)
    }
    
    print("Tworzę pliki testowe...")
    for filename, size in test_files.items():
        filepath = sample_dir / filename
        # Utwórz plik danej wielkości
        with open(filepath, 'wb') as f:
            f.write(os.urandom(size))
        print(f"✓ {filename} ({size // 1024} KB)")
    
    print(f"\nUtworzono {len(test_files)} plików testowych w: {sample_dir}")

if __name__ == "__main__":
    create_test_files()
