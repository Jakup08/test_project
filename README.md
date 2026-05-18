# 🎬 Media File Sorter

Profesjonalne narzędzie do automatycznego sortowania i organizacji multimediów. Sortuje pliki wideo, audio i fotografie do oddzielnych katalogów na podstawie rozszerzenia.

## ✨ Główne cechy

- 🎯 **26+ rozszerzeń** - Obsługuje video, audio i fotografie
- 📊 **Szczegółowe statystyki** - Raport liczby i rozmiaru plików
- 💾 **Format rozmiarów** - Automatyczne skalowanie (B, KB, MB, GB, TB)
- 🔄 **Rekurencyjne przeszukiwanie** - Opcja dla podkatalogów
- 🛡️ **Bezpieczne** - Obsługa błędów dla każdego pliku
- ⚡ **Szybkie** - Jedno polecenie do uruchomienia
- 📁 **Organizacja** - Każde rozszerzenie w osobnym folderze

## 📦 Obsługiwane typy plików

### 🎥 Video
`.mp4` `.mkv` `.avi` `.mov` `.flv` `.dav` `.webm` `.m4v`

### 🎵 Audio
`.mp3` `.wav` `.aac` `.flac` `.m4a` `.ogg` `.wma` `.opus`

### 📸 Fotografie
`.jpg` `.jpeg` `.png` `.gif` `.bmp` `.webp` `.tiff` `.heic` `.raw`

## 🚀 Szybki start

### Wymagania
- Python 3.6+ (brak dodatkowych zależności)
- Uprawnienia do czytania/pisania w katalogach

### Instalacja
```bash
git clone https://github.com/Jakup08/test_project.git
cd test_project
```

## 💡 Przykłady użycia

### 1. Sortuj z domyślnymi ustawieniami
```bash
python sorter.py
```
Sortuje z `sample_files/` do `multimedialne/`

### 2. Własne katalogi
```bash
python sorter.py --src ~/Downloads --dest ~/Media
```

### 3. Rekurencyjne (przeszukuj podkatalogi)
```bash
python sorter.py --recursive
```

### 4. Tylko określone rozszerzenia
```bash
python sorter.py --exts mp4 mkv wav mp3
```

### 5. Utwórz pliki testowe
```bash
python sorter.py --test-create
```

### 6. Wyświetl dostępne typy
```bash
python sorter.py --list-types
```

## 📖 Opcje wiersza poleceń

| Opcja | Opis | Domyślnie |
|-------|------|----------|
| `--src` | Katalog źródłowy | `sample_files` |
| `--dest` | Katalog docelowy | `multimedialne` |
| `--exts` | Lista rozszerzeń | Wszystkie (26+) |
| `--recursive` | Przeszukuj podkatalogi | Nie |
| `--test-create` | Utwórz pliki testowe | - |
| `--list-types` | Wyświetl dostępne typy | - |

## 🔧 Scenariusze

### Scenario 1: Sortowanie Downloads
```bash
python sorter.py --src ~/Downloads --dest ~/MediaLibrary --recursive
```

### Scenario 2: Test z przykładowymi plikami
```bash
# 1. Utwórz pliki testowe
python sorter.py --test-create

# 2. Sortuj je
python sorter.py

# 3. Sprawdź strukturę
tree multimedialne/
```

**Wynik:**
```
multimedialne/
├── MP4/
│   └── video1.mp4
├── WAV/
│   └── music.wav
├── JPG/
│   └── photo1.jpg
└── ...
```

## 📂 Struktura projektu

```
test_project/
├── sorter.py                    # ✨ GŁÓWNY PLIK (scalony)
├── README.md                    # Dokumentacja
├── sample_files/                # Przykładowe pliki
├── multimedialne/               # Wynik sortowania
│
└── sorter/                      # Katalog PoC-ów (archiwum)
    ├── poc_mp4.py               # PoC 1: tylko .mp4
    ├── poc_multi.py             # PoC 2: wiele rozszerzeń
    ├── poc_large_multi.py       # PoC 3: duże pliki + statystyki
    └── create_test_files.py     # Generator testów
```

## 🐛 Troubleshooting

### "Katalog nie istnieje"
```bash
ls -la /path/to/directory
```

### "Permission denied"
```bash
chmod +x sorter.py
```

### Pliki nie były sortowane
```bash
python sorter.py --list-types
```

## 💡 Wskazówki

✅ Zawsze rób kopię zapasową przed sortowaniem  
✅ Uruchom z `--test-create` najpierw  
✅ Używaj `--recursive` ostrożnie  
✅ Format rozmiarów automatycznie się dostosowuje  

## 📝 Notatki

- ✓ Czysty Python 3.6+ - brak zależności
- ✓ Bezpieczne dla dużych plików
- ✓ Obsługuje znaki diakrytyczne
- ✓ Pliki są **przenoszące** (nie kopiowane)
- ✓ Tworzy katalogi jeśli nie istnieją

## 📄 Licencja

MIT

## 👤 Autor

Jakup08 - 2026

---

**Ostatnia aktualizacja:** 2026-05-18  
**Wersja:** 1.0.0 (scalony POC)
