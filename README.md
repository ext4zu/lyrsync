# synced-lyrics - Synced Lyrics for Your Terminal

## NEW: Use synced-itv for interactive version!

---

## Requirements
- **Python** (3.7+)  
- **Any audio player** 

---

## Installation
1. Clone the repo:
```bash
git clone https://github.com/zhu-ha/synced-lyrics.git
cd synced-lyrics
python synced-lyrics.py
```

---


## How to use

Basic usage with flags:

- Place your .lrc file and audio file anywhere on your system. The script accepts a path to the .lrc file and an optional audio file path.

Examples:

- Display lyrics and play audio once (using SoX):
```bash
python synced-lyrics.py -l path/to/lyrics.lrc -a path/to/song.flac
```

- Loop the lyrics/audio twice:
```bash
python synced-lyrics.py -l path/to/lyrics.lrc -a path/to/song.flac --loop 2
```

- Loop infinitely:
```bash
python synced-lyrics.py -l path/to/lyrics.lrc -a path/to/song.flac --loop inf
```


