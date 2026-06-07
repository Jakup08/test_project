# Media File Sorter

Media File Sorter to prosty skrypt w Pythonie do sortowania plików na podstawie rozszerzeń.
Domyślnie skrypt pobiera pliki z katalogu `sample_files/` i przenosi je do katalogu `sorted_media/`, tworząc podkatalogi dla kategorii (video, audio, obrazy, dokumenty, kod, archiwa).

## Główne cechy

- Obsługa typowych rozszerzeń dla video, audio, obrazów, dokumentów, archiwów i kodu.
- Statystyki: liczba przeniesionych plików i łączny rozmiar.
- Możliwość rekurencyjnego przeszukiwania podkatalogów.
- Bezpieczeństwo: skrypt unika nadpisywania plików (dodaje sufiks `_1`, `_2` w razie konfliktu).

## Obsługiwane kategorie i rozszerzenia (wybrane)

Video: .mp4 .mkv .avi .mov .flv .dav .webm .m4v .wmv .3gp .m3u8

Audio: .mp3 .wav .aac .flac .m4a .ogg .wma .opus .alac .aiff

Obrazy: .jpg .jpeg .png .gif .bmp .webp .tiff .heic .raw .svg .ico .psd

Dokumenty: .pdf .docx .doc .xlsx .xls .pptx .ppt .txt .odt .rtf .csv .json .xml

Archiwa: .zip .rar .7z .tar .gz .bz2 .iso .dmg

Kod: .py .js .ts .java .cpp .c .h .html .css .php .go .rs .rb .sh

(Pełna lista rozszerzeń dostępna w kodzie `sorter.py`.)

## Wymagania

- Python 3.6 lub nowszy
- Brak dodatkowych zewnętrznych zależności

## Szybki start

1. Sklonuj repozytorium lub przejdź do katalogu projektu:
```bash
git clone https://github.com/Jakup08/test_project.git
cd test_project
```

2. (Opcjonalnie) utwórz środowisko wirtualne:
```bash
python -m venv venv
# Windows (PowerShell):
venv\Scripts\Activate.ps1
# Windows (cmd):
venv\Scripts\activate.bat
# Linux/macOS:
source venv/bin/activate
```

3. Utwórz przykładowe pliki testowe:
```bash
python sorter.py --test-create
```

4. Uruchom sortowanie (domyślnie `sample_files` → `sorted_media`):
```bash
python sorter.py
```

5. Sprawdź wynik:
```bash
ls -la sorted_media
ls -la sample_files
```

## Opcje

- `--src` : katalog źródłowy (domyślnie `sample_files`)
- `--dest`: katalog docelowy (domyślnie `sorted_media`)
- `--exts`: lista rozszerzeń do sortowania (np. `--exts mp4 mp3 txt`)
- `--recursive`: przeszukuj podkatalogi
- `--test-create`: utwórz pliki testowe w `--src`
- `--list-types`: wyświetl dostępne typy/rozszerzenia

## Przywracanie plików

Jeśli chcesz cofnąć ostatnie przeniesienia (przenieść pliki z `sorted_media` do `sample_files`), użyj:
```bash
python move_files_back.py
```

## Uwagi

- Skrypt przenosi pliki (nie kopiuje). Zrób kopię zapasową ważnych plików, jeśli to konieczne.
- Katalog docelowy nie może być podkatalogiem katalogu źródłowego (skrypt to sprawdza i zatrzyma działanie).

## Licencja

MIT

---
