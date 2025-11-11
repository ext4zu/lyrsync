# synced-lyrics - Terminal-Based Synced Lyrics Viewer

A command-line tool for displaying synced lyrics alongside audio playback.  
Supports `.lrc` files and any audio format playable by your system.

---

## Requirements

- Python 3.7 or later  
- Any audio player (e.g., SoX, VLC)

---

## Installation

Clone the repository and run the script:
```bash
git clone https://github.com/zhu-ha/synced-lyrics.git
cd synced-lyrics
python synced-lyrics.py
```

---

## Usage

Run the script with flags to specify your lyrics and audio files:
```bash
python synced-lyrics.py -l path/to/lyrics.lrc -a path/to/song.flac
```

### Options

- `--loop 2` : Loop playback and lyrics display twice  
- `--loop inf` : Loop indefinitely until manually stopped

Place your `.lrc` and audio files anywhere on your system. The script accepts full paths to both.

---

## Notes

- Audio playback is optional; lyrics will display even without an audio file.  
- Compatible with any player that can be invoked from the command line.  
- For an interactive version, use the companion tool `synced-itv`.

---

## Exit

Press `Ctrl + C` to stop playback and exit the program at any time.
