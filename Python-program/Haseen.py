import time
import sys

def print_lyrics():
    Lyrics=[
        "Tere ishq da jaam hassen hai",
        "Subh hseen meri shaam haseen hai",
        "Ae bematlabi zindagi",
        "jado di tere naam haseen hai",
        "Tere ishq da jaam hassen hai",
        "Subh hseen meri shaam haseen hai",
        "Ae bematlabi zindagi",
        "jado di tere naam haseen hai",
    ]

    delays = [1.6, 1.6, 1.6, 1.8,1.6, 1.6, 1.6, 1.8]
    print("Haseen: \n")
    time.sleep(1.2)
    for i, line in enumerate(Lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        if i < len(delays):
            time.sleep(delays[i])
        else:
            time.sleep(0.5)
print_lyrics()
