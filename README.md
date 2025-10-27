# synced-lyrics 🎵

**Synced lyrics for your terminal!**

A small, terminal-first utility to display synchronized lyrics while you play music — clean, lightweight, and easy to use.

---

## ✨ Highlights
- **Terminal-friendly** synced lyric display  
- **Minimal dependencies** and easy setup  
- Supports timed lyrics (LRC) for accurate syncing

---

## ✅ Requirements
- **Python** (3.7+)  
- **SoX** (Sound eXchange) — used for audio handling

---

## 🚀 Installation
1. Clone the repo:
```bash
git clone https://github.com/zhu-ha/synced-lyrics.git
cd synced-lyrics
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate.bat # Windows
```

3. Install Python dependencies (if available):
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the script from the repository root. Replace the example command below with the actual script and file names in this repo:

```bash
python sync_lyrics.py --audio path/to/song.mp3 --lyrics path/to/lyrics.lrc
```

Tips:
- Use **.lrc** lyrics files for timed (synced) displays.
- You can pipe audio through SoX or use local files depending on implementation.

---

## 🧩 Example
If you have `song.mp3` and `song.lrc` in the repo root:
```bash
python sync_lyrics.py --audio song.mp3 --lyrics song.lrc
```

---

## 🤝 Contributing
Contributions are welcome! If you spot an issue or want to improve the README (for example, to include exact usage or more examples), please open an issue or submit a pull request.

If you'd like, I can:
- Add badges (CI, PyPI) — if you tell me the services
- Add a detailed example using the exact script/flags present in the repo
- Commit this README directly to the repository (just tell me to apply)

---

## 📄 License
This project is open source — add your preferred license here (e.g., MIT, Apache-2.0).

---
