# 🎬 Media File Sorter

Profesjonalne narzędzie do automatycznego sortowania i organizacji plików według kategorii. Sortuje pliki video, audio, obrazy, dokumenty, kod i archiwa do oddzielnych katalogów na podstawie rozszerzenia.

## ✨ Główne cechy

- 🎯 **68+ rozszerzeń** - Video, audio, obrazy, dokumenty, kod, archiwa
- 📊 **Kategorie zamiast rozszerzeń** - Łatwa organizacja (obrazy/ dokumenty/ video/ itp.)
- 📋 **Szczegółowe statystyki** - Raport liczby i rozmiaru plików po kategoriach
- 🔄 **Rekurencyjne przeszukiwanie** - Opcja dla podkatalogów
- 🛡️ **Bezpieczne** - Obsługa błędów dla każdego pliku
- ⚡ **Szybkie** - Jedno polecenie do uruchomienia
- 📁 **Inteligentna organizacja** - Każda kategoria w osobnym folderze

## 📦 Obsługiwane kategorie i rozszerzenia

### 🎥 Video
`.mp4` `.mkv` `.avi` `.mov` `.flv` `.dav` `.webm` `.m4v` `.wmv` `.3gp` `.m3u8`

### 🎵 Audio
`.mp3` `.wav` `.aac` `.flac` `.m4a` `.ogg` `.wma` `.opus` `.alac` `.aiff`

### 📸 Obrazy
`.jpg` `.jpeg` `.png` `.gif` `.bmp` `.webp` `.tiff` `.heic` `.raw` `.svg` `.ico` `.psd`

### 📄 Dokumenty
`.pdf` `.docx` `.doc` `.xlsx` `.xls` `.pptx` `.ppt` `.txt` `.odt` `.rtf` `.csv` `.json` `.xml`

### 📦 Archiwa
`.zip` `.rar` `.7z` `.tar` `.gz` `.bz2` `.iso` `.dmg`

### 💻 Kod
`.py` `.js` `.ts` `.java` `.cpp` `.c` `.h` `.html` `.css` `.php` `.go` `.rs` `.rb` `.sh`

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
Sortuje z `sample_files/` do `sorted_media/`

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
| `--src` | Katalog źródłowy | `sample_files` |
| `--dest` | Katalog docelowy | `sorted_media` |
| `--exts` | Lista rozszerzeń do sortowania | Wszystkie (68+) |
| `--recursive` | Przeszukuj podkatalogi | Nie |
| `--test-create` | Utwórz pliki testowe z wielu kategorii | - |
| `--list-types` | Wyświetl dostępne kategorie i rozszerzenia | - |

## 🔧 Scenariusze

### Scenariusz 1: Sortowanie Downloads
```bash
python sorter.py --src ~/Downloads --dest ~/MediaLibrary --recursive
```

### Scenariusz 2: Test z przykładowymi plikami
```bash
# 1. Utwórz pliki testowe
python sorter.py --test-create

# 2. Sortuj je
python sorter.py

# 3. Sprawdź strukturę
tree sorted_media/
```

**Wynik:**
```
sorted_media/
├── video/
│   ├── film.mp4
│   ├── film.mkv
│   └── recording.dav
├── audio/
│   ├── piosenka.mp3
│   └── muzyka.wav
├── obrazy/
│   ├── foto.jpg
│   └── zdjecie.png
├── dokumenty/
│   └── dokument.pdf
├── archiwum/
│   └── pliki.zip
└── kod/
    └── skrypt.py
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

## 🐛 Obsługa błędów

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
