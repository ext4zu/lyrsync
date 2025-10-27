import time
import os
import math
import subprocess

//Example song : Fashion by CORTIS
    
//Color coding here
    
colors = {
    "Seonghyeon": "[93m",
    "James": "[92m",
    "Martin": "[91m",
    "Juhoon": "[94m",
    "Keonho": "[95m",
    "All": "[96m",
    "Default": "[0m"
}
//.lrc text here
lyrics = [
    (6.041, "nae ti, 5 bucks", "Keonho"),
    (7.492, "bajineun, manwon", "Keonho"),
    (9.05, "My vision, myeot eoks", "Keonho"),
    (10.563, "myeot jos, Bezos", "Keonho"),
    (12.233, "Dongmyo, Wassup", "Juhoon"),
    (13.68, "Hongdae, Wassup", "Juhoon"),
    (15.214, "I make them famous", "Keonho"),
    (16.786, "I call that, Fashion", "Seonghyeon"),
    (18.302, "Fashion, Fashion", "Seonghyeon"),
    (19.785, "Fashion, Fashion", "Seonghyeon"),
    (21.416, "Fashion, Fashion", "Seonghyeon"),
    (22.915, "Fashion, Fashion", "Seonghyeon"),
    (24.608, "nae ti, 5 bucks", "Juhoon"),
    (26.106, "bajineun, manwon", "Juhoon"),
    (27.638, "Let’s get it, Let’s go", "Juhoon"),
    (29.238, "Fashion, Fashion", "Juhoon"),
    (30.616, "angeonho, naega san ot bogo mworago malhaedo", "Martin"),
    (32.454, "jikyeo nae gojip", "Martin"),
    (33.599, "hureucheu jjimhaenoheun sangpume isseotdeon belteuneun", "Martin"),
    (35.565, "now on my heori", "Martin"),
    (36.719, "Sorry my granny", "Martin"),
    (37.893, "yojeum wae an oni", "Martin"),
    (38.702, "seopasin dongmyo halmeoni", "Martin"),
    (39.772, "yeogin bihaenggi", "Martin"),
    (41.033, "LAeseo aelbeomeul kkeutnaego", "Martin"),
    (42.162, "meositge dorawa", "Martin"),
    (42.933, "back on my swag", "Martin"),
    (44.529, "oehwa talk, hwanyul olla maeil", "James"),
    (47.603, "guje pan, Got me looking fresh", "James"),
    (50.699, "Pull up boys, syaksyak geulgeonae", "James"),
    (53.814, "'bintijijeoseu'", "James"),
    (55.772, "dongmyoeseo moyeo, machi semina", "Seonghyeon"),
    (58.887, "hongdaeeseo moyeo, urin set it off", "Seonghyeon"),
    (61.972, "cheongdamdong hangaundekkaji spreading out", "Seonghyeon"),
    (64.898, "Squad is on the way but we can’t wrap it up", "Seonghyeon"),
    (67.913, "nae ti, 5 bucks", "James"),
    (69.429, "bajineun, manwon", "James"),
    (70.876, "My vision, myeot eoks", "James"),
    (72.49, "myeot jos, Bezos", "James"),
    (74.212, "Dongmyo, Wassup", "Seonghyeon"),
    (75.675, "Hongdae, Wassup", "Seonghyeon"),
    (77.149, "I make them famous", "James"),
    (78.698, "I call that, Fashion", "Seonghyeon"),
    (80.305, "Fashion, Fashion", "Seonghyeon"),
    (81.712, "Fashion, Fashion", "Seonghyeon"),
    (83.343, "Fashion, Fashion", "Seonghyeon"),
    (84.843, "Fashion, Fashion", "Seonghyeon"),
    (86.489, "nae ti, 5 bucks", "Keonho"),
    (88.025, "bajineun, manwon", "Keonho"),
    (89.637, "Let’s get it, Let’s go", "Juhoon"),
    (91.139, "Fashion, Fashion", "Juhoon"),
    (92.737, "simjangi pop out", "Martin"),
    (94.161, "cheonnune baro cop cop", "Martin"),
    (96.302, "guje jjambap", "Martin"),
    (97.232, "sammawonjjari jamba", "Martin"),
    (99.323, "Feel like rockstar", "Martin"),
    (100.406, "hwak Met Gala-ro galla, Let’s go", "Martin"),
    (102.544, "Top Designers,", "Martin"),
    (103.502, "hongdae matbogo hwanjang, Fashion", "Martin"),
    (106.029, "Come and try", "Seonghyeon"),
    (106.834, "dongmyo saenghwareseo nan", "Seonghyeon"),
    (108.402, "cheryeogeul mani dakkana", "Seonghyeon"),
    (109.959, "Mosh Pit haneun beop baewonwa", "Seonghyeon"),
    (111.459, "baewobwa, baewobwa", "James"),
    (113.042, "neodo ppalli baewobwa", "James"),
    (114.512, "ot mudeom sok dasi taeeona", "James"),
    (116.139, "bintijijeoseu, came alive", "James"),
    (117.713, "dongmyoeseo moyeo, machi semina", "Seonghyeon"),
    (120.82, "hongdaeeseo moyeo, urin set it off", "Seonghyeon"),
    (123.897, "cheongdamdong hangaundekkaji spreading out", "Seonghyeon"),
    (126.89, "Squad is on the way but we can’t wrap it up", "Seonghyeon"),
    (129.892, "nae ti, 5 bucks", "Keonho"),
    (131.398, "bajineun, manwon", "Keonho"),
    (132.913, "My vision, myeot eoks", "Keonho"),
    (134.353, "myeot jos, Bezos", "Keonho"),
    (136.065, "Dongmyo, Wassup", "Juhoon"),
    (137.658, "Hongdae, Wassup", "Juhoon"),
    (139.108, "I make them famous", "Keonho"),
    (140.648, "I call that, Fashion", "Seonghyeon"),
    (142.245, "Fashion, Fashion", "All"),
    (143.683, "Fashion, Fashion", "All"),
    (145.314, "Fashion, Fashion", "All"),
    (146.767, "Fashion, Fashion", "All"),
    (148.36, "Fashion, Fashion", "All"),
    (149.979, "Fashion, Fashion", "All"),
    (151.476, "Fashion, Fashion", "All"),
    (152.927, "Fashion, Fashion", "All"),
    (154.658, "Fashion, Fashion", "All"),
    (156.174, "Fashion, Fashion", "All"),
    (157.697, "Fashion, Fashion", "All"),
    (159.301, "Fashion, Fashion", "All"),
    (160.694, "Fashion, Fashion", "All"),
    (162.238, "Fashion, Fashion", "All"),
    (163.781, "Fashion, Fashion", "All"),
    (165.44, "Fashion, Fashion", "All")
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_lyrics():
    flac_file_path = "/audio/path/here"

    input("Press Enter to start...")
    
    try:
        audio_process = subprocess.Popen(["play", flac_file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print(f"Error: The 'play' command is not found. Please install 'sox'.")
        return
    except Exception as e:
        print(f"Error playing audio: {e}")
        return

    start_time = time.time()
    first_lyric_time = lyrics[0][0]

    while time.time() - start_time < first_lyric_time:
        remaining_time = first_lyric_time - (time.time() - start_time)
        if remaining_time > 0:
            clear_screen()
            terminal_width, terminal_height = os.get_terminal_size()
            countdown_number = str(math.ceil(remaining_time))
            horizontal_padding = (terminal_width - len(countdown_number)) // 2
            vertical_padding = (terminal_height - 1) // 2
            print("
" * vertical_padding, end="")
            print(" " * horizontal_padding + countdown_number)
            time.sleep(0.1)

    for i, (timestamp, line, member) in enumerate(lyrics):
        while time.time() - start_time < timestamp:
            time.sleep(0.1)
        
        clear_screen()
        terminal_width, terminal_height = os.get_terminal_size()
        
        color = colors.get(member, colors["Default"])
        colored_line = f"{color}{line}{colors['Default']}"
        
        horizontal_padding = (terminal_width - len(line)) // 2
        vertical_padding = (terminal_height - 1) // 2

        print("
" * vertical_padding, end="")
        print(" " * horizontal_padding + colored_line)

    audio_process.terminate()

if __name__ == "__main__":
    display_lyrics()
