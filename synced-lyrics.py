#!/usr/bin/env python3
"""
synced-lyrics.py

Usage examples:
  # Using sox (play) - no extra flags needed for the player:
  python synced-lyrics.py -l path/to/lyrics.lrc -a path/to/song.flac --loop 2

  # Using a non-sox player (provide --player):
  python synced-lyrics.py -l lyrics.lrc -a song.mp3 --player ffplay --loop inf

Features:
- Parses standard .lrc timestamped lyrics [mm:ss.xx]
- Accepts --lrc / -l and --audio / -a paths
- Optional --player flag only required when not using sox/play (default is sox 'play')
- Supports --loop N (integer) or --loop inf for infinite looping
- Plain centered lyrics output (no color coding)
- Ctrl+C safely terminates audio and exits
"""

import argparse
import re
import time
import os
import sys
import math
import subprocess
import signal

TIMESTAMP_RE = re.compile(r'\[(\d+):([0-5]?\d(?:\.\d+)?)\]')


def parse_lrc(lrc_path):
    entries = []
    try:
        with open(lrc_path, 'r', encoding='utf-8') as f:
            for raw in f:
                line = raw.strip()
                if not line:
                    continue
                timestamps = TIMESTAMP_RE.findall(line)
                if not timestamps:
                    continue
                text = TIMESTAMP_RE.sub('', line).strip()
                if not text:
                    continue
                for m in timestamps:
                    minutes = int(m[0])
                    seconds = float(m[1])
                    total = minutes * 60 + seconds
                    entries.append((total, text))
    except FileNotFoundError:
        print(f"Error: .lrc file not found at: {lrc_path}")
        sys.exit(2)
    except Exception as e:
        print(f"Error reading .lrc file: {e}")
        sys.exit(2)

    entries.sort(key=lambda x: x[0])
    return entries


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def center_display(text):
    try:
        terminal_width, terminal_height = os.get_terminal_size()
    except OSError:
        terminal_width, terminal_height = 80, 24

    lines = text.splitlines()
    max_width = max((len(l) for l in lines), default=0)
    horizontal_padding = max((terminal_width - max_width) // 2, 0)
    vertical_padding = max((terminal_height - len(lines)) // 2, 0)

    print("\n" * vertical_padding, end="")
    for line in lines:
        print(" " * horizontal_padding + line)


def build_player_cmd(player, audio_path):
    if player == 'ffplay':
        return ['ffplay', '-nodisp', '-autoexit', '-loglevel', 'quiet', audio_path]
    elif player == 'mpv':
        return ['mpv', '--no-video', '--really-quiet', audio_path]
    else:
        # default to sox/play
        return ['play', audio_path]


def play_audio(player_cmd):
    try:
        p = subprocess.Popen(player_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return p
    except FileNotFoundError:
        print(f"Error: audio player not found: {player_cmd[0]}")
        return None
    except Exception as e:
        print(f"Error launching audio player: {e}")
        return None


def display_loop(lyrics_entries):
    if not lyrics_entries:
        print("No lyrics to display.")
        return

    start_time = time.time()
    first_ts = lyrics_entries[0][0]

    while True:
        elapsed = time.time() - start_time
        remaining = first_ts - elapsed
        if remaining <= 0:
            break
        clear_screen()
        countdown_number = str(math.ceil(remaining))
        center_display(countdown_number)
        time.sleep(0.1)

    for timestamp, text in lyrics_entries:
        while True:
            elapsed = time.time() - start_time
            if elapsed >= timestamp:
                break
            time.sleep(0.05)
        clear_screen()
        center_display(text)

    time.sleep(0.5)


def parse_loop_value(loop_value):
    if loop_value is None:
        return 1
    v = str(loop_value).strip().lower()
    if v in ('inf', 'infinite', '0', '-1'):
        return None
    try:
        n = int(v)
        if n <= 0:
            return None
        return n
    except Exception:
        return None


def main():
    parser = argparse.ArgumentParser(description="Display synced lyrics from a .lrc file while playing audio.")
    parser.add_argument('-l', '--lrc', required=True, help="Path to .lrc file with timestamps.")
    parser.add_argument('-a', '--audio', required=False, help="Path to audio file (optional). If not provided, lyrics will display without audio.")
    parser.add_argument('--player', default=None, help="(Optional) Player command to use if not using sox/play. Examples: ffplay, mpv")
    parser.add_argument('--loop', default='1', help="How many times to play/loop: integer or 'inf' for infinite (default 1).")
    args = parser.parse_args()

    lyrics = parse_lrc(args.lrc)
    loop_count = parse_loop_value(args.loop)

    player_cmd_template = None
    if args.audio:
        # If user didn't supply --player, assume sox 'play' without requiring flag
        chosen_player = args.player if args.player else 'play'
        player_cmd_template = build_player_cmd(chosen_player, args.audio)

        # Only pre-check existence if user explicitly provided a non-sox player
        if args.player:
            from shutil import which
            if which(player_cmd_template[0]) is None:
                print(f"Warning: player '{player_cmd_template[0]}' not found in PATH. You may need to install it or choose another --player.")
                # We continue; play_audio will handle failure when launching.

    audio_processes = []

    def sigint_handler(signum, frame):
        for p in audio_processes:
            if p and p.poll() is None:
                try:
                    p.terminate()
                except Exception:
                    pass
        print("\nInterrupted. Exiting.")
        sys.exit(1)

    signal.signal(signal.SIGINT, sigint_handler)

    try:
        while True:
            if player_cmd_template:
                audio_proc = play_audio(player_cmd_template)
                if audio_proc:
                    audio_processes.append(audio_proc)
                else:
                    audio_proc = None
            else:
                audio_proc = None

            # Run the lyric display synchronized to the start time.
            display_loop(lyrics)

            # WAIT for the audio to finish naturally before proceeding to loop/exit.
            # This ensures we don't stop/loop while the audio is still playing.
            if audio_proc and audio_proc.poll() is None:
                try:
                    audio_proc.wait()
                except KeyboardInterrupt:
                    # If user hits Ctrl+C while waiting, clean up and exit.
                    sigint_handler(None, None)

            # If loop_count is None -> infinite
            if loop_count is None:
                continue
            else:
                loop_count -= 1
                if loop_count <= 0:
                    break

    except KeyboardInterrupt:
        sigint_handler(None, None)


if __name__ == "__main__":
    main()
