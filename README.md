# synced-lyrics

**Synced lyrics for your terminal!**

---

## Requirements
- **Python** (3.7+)  
- **SoX** (Sound eXchange) — used for audio handling

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

Basic usage with SoX (default):

- Place your .lrc file and audio file anywhere on your system. The script accepts a path to the .lrc file and an optional audio file path.
- SoX's `play` command is used by default, so you don't need to pass a player flag when using SoX.

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

Using a non-SoX player (e.g., ffplay or mpv):

- If you prefer another player, provide the --player flag. The script will only warn if the player binary is not found when you explicitly pass --player.

Examples:

```bash
python synced-lyrics.py -l lyrics.lrc -a song.mp3 --player ffplay
python synced-lyrics.py -l lyrics.lrc -a song.mp3 --player mpv --loop 3
```

Display lyrics without audio:

```bash
python synced-lyrics.py -l path/to/lyrics.lrc
```

.lrc format

- The script parses standard .lrc timestamp lines like:
```
[00:12.34]This is the lyric line
[00:45.00][00:47.50]Repeated-lyric for multiple timestamps
```
- Lines with multiple timestamps create multiple synchronized entries.

Notes

- If the audio player introduces startup latency you can use a different player (mpv/ffplay) or request an offset feature to fine-tune synchronization.
- The script centers plain lyrics in the terminal and does not use color coding.

---

Feel free to open an issue if you'd like me to add example .lrc files, recommend SoX installation steps for different OSes, or add a sample usage section with screenshots.