# lyrsync - Terminal Synced Lyrics Viewer

A command-line tool for displaying time-synced `.lrc` lyrics in your terminal alongside audio playback.  
Supports most audio formats and auto-detects available players like **mpv**, **ffplay**, **vlc**, **afplay**, and **sox**.

---

## Requirements

- Python 3.7 or later  
- At least one audio player installed and available in your system `PATH`:
  - `mpv`, `ffplay`, `afplay`, `vlc`, `cvlc`, `mplayer`, or `play` (SoX)

---

## Usage

Clone the repository and run the script:
```bash
git clone https://github.com/ext4zu/lyrsync.git
cd lyrsync
python3 lyrsync.py
```
### Steps

1. Enter the **audio file path** (drag and drop or type manually).  
2. Enter the **.lrc lyrics file path**.  
3. Specify how many times to play OR;
   - `1` for single playback  
   - `0` for infinite loop  
   - Any positive integer for repeated playback  
4. The lyrics will be displayed in sync with the audio, centered in your terminal.

---

## Supported Players

The script auto-detects and uses the first available player from this list:

| Player     | Notes                          |
|------------|--------------------------------|
| mpv        | Recommended for most systems   |
| ffplay     | Lightweight and fast           |
| afplay     | macOS built-in                 |
| vlc/cvlc   | Cross-platform support         |
| mplayer    | Terminal-friendly              |
| play       | Provided by SoX                |

---

## Notes

- `.lrc` files must contain valid timestamped lyrics.  
- The script attempts multiple path formats to resolve user input.  
- If no player is found, it defaults to `play` (SoX), which may fail if not installed.  
- Lyrics are displayed with countdown and centered formatting for readability.  
- You can interrupt playback anytime with `Ctrl + C`.

---

## Exit

Press `Ctrl + C` to stop playback and exit the program safely.
