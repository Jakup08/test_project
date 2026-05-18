# POC: Sortowanie wielu plików (duże rozszerzenia)

## Opis
POC dla sortowania wielu plików o różnych rozszerzeniach do oddzielnych katalogów. Obsługuje:
- ✅ Wiele rozszerzeń multimedianych (wideo, audio, foto)
- ✅ Duże pliki (obsługa B, KB, MB, GB, TB)
- ✅ Sortowanie do oddzielnych katalogów po rozszerzeniu
- ✅ Statystyki (liczba plików, rozmiar)
- ✅ Rekurencyjne przeszukiwanie (opcjonalne)
- ✅ Obsługa błędów

## Domyślne rozszerzenia

### Video
`.mp4`, `.dav`, `.mkv`, `.avi`, `.mov`, `.flv`

### Audio
`.mp3`, `.wav`, `.aac`, `.flac`, `.m4a`

### Foto
`.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.tiff`

## Użycie

### 1. Podstawowe sortowanie
```bash
python sorter/poc_large_multi.py
```
Sortuje z `sample_files/` do `multimedialne/`

### 2. Własne katalogi
```bash
python sorter/poc_large_multi.py --src my_folder --dest sorted_media
```

### 3. Rekurencyjne (podkatalogi)
```bash
python sorter/poc_large_multi.py --recursive
```

### 4. Własne rozszerzenia
```bash
python sorter/poc_large_multi.py --exts mp4 mkv webm aac
```

### 5. Wyświetl domyślne rozszerzenia
```bash
python sorter/poc_large_multi.py --list-exts
```

## Wynik sortowania

Pliki są sortowane do struktury:
```
multimedialne/
├── MP4/
│   └── video.mp4
├── DAV/
│   └── recording.dav
├── JPG/
│   └── photo.jpg
└── ...
```

## Test

### 1. Utwórz pliki testowe
```bash
python sorter/create_test_files.py
```

### 2. Uruchom sortowanie
```bash
python sorter/poc_large_multi.py --src sample_files --dest multimedialne_sorted
```

### 3. Sprawdź strukturę
```bash
tree multimedialne_sorted
```

## Statystyki

POC wyświetla podsumowanie:
- Liczba przeniesiony plików
- Całkowity rozmiar
- Statystyki po każdym rozszerzeniu
- Błędy (jeśli wystąpią)

## Przykład wyjścia
```
Znaleziono 9 plik(ów), sortowanie...
✓ video.mp4 (100.00 KB) -> MP4/
✓ music.wav (5.00 MB) -> WAV/
✓ photo.jpg (50.00 KB) -> JPG/

============================================================
PODSUMOWANIE
============================================================
Przeniesiono: 8 plik(ów)
Całkowity rozmiar: 6.97 MB

Statystyki po rozszerzeniu:
  .mp4       -   1 plik(ów),    100.00 KB
  .wav       -   1 plik(ów),      5.00 MB
  .jpg       -   1 plik(ów),     50.00 KB
```

## Cechy

✅ **Format rozmiarów** - Automatyczne skalowanie (B, KB, MB, GB, TB)
✅ **Oddzielne katalogi** - Każde rozszerzenie w osobnym folderze
✅ **Statystyki szczegółowe** - Raport po każdym rozszerzeniu
✅ **Obsługa dużych plików** - Brak limitów
✅ **Rekurencyjne** - Opcja do przeszukiwania podkatalogów
✅ **Bezpieczne** - Obsługa błędów dla każdego pliku

---

**Pliki:**
- `poc_large_multi.py` - Główny POC dla wielu plików i rozszerzeń
- `create_test_files.py` - Generator plików testowych
- `poc_mp4.py` - POC dla .mp4
- `poc_multi.py` - POC dla wielu rozszerzeń
