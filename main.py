import pyautogui
import functools
import time
import track
import score_parser

time.sleep(5)
pyautogui.PAUSE = 0

play_funcs = {
    0: lambda: 0,
    1: functools.partial(pyautogui.press, 'z'),
    2: functools.partial(pyautogui.press, 'x'),
    3: functools.partial(pyautogui.press, 'c'),
    4: functools.partial(pyautogui.press, 'v'),
    5: functools.partial(pyautogui.press, 'b'),
    6: functools.partial(pyautogui.press, 'n'),
    7: functools.partial(pyautogui.press, 'm'),
    8: functools.partial(pyautogui.press, 'a'),
    9: functools.partial(pyautogui.press, 's'),
    10: functools.partial(pyautogui.press, 'd'),
    11: functools.partial(pyautogui.press, 'f'),
    12: functools.partial(pyautogui.press, 'g'),
    13: functools.partial(pyautogui.press, 'h'),
    14: functools.partial(pyautogui.press, 'j'),
    15: functools.partial(pyautogui.press, 'q'),
    16: functools.partial(pyautogui.press, 'w'),
    17: functools.partial(pyautogui.press, 'e'),
    18: functools.partial(pyautogui.press, 'r'),
    19: functools.partial(pyautogui.press, 't'),
    20: functools.partial(pyautogui.press, 'y'),
    21: functools.partial(pyautogui.press, 'u')
}

score_file_list = ['score_1.txt', 'score_2.txt']
tracks = []
for filename in score_file_list:
    with open(filename, 'r') as f:
        score_txt = f.read().split()
        score_pri, tick_duration = score_parser.parse(score_txt)
        tracks.append(track.Track(score_pri, play_funcs))


player = track.Player(tracks, tick_duration)
player.play()
