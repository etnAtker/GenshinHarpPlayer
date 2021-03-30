# import functools
import threading


class Track:
    def __init__(self, score, play_funcs):
        self.score = zip(score['notes'], score['duration'])
        self.play_funcs = play_funcs
        self.tick = 0

    def step(self):
        try:
            if self.tick == 0:
                note, duration = next(self.score)
                self.play_funcs[note]()
                self.tick = duration
            self.tick -= 1
        except StopIteration:
            return


class Player:
    def __init__(self, tracks, tick_duration):
        self.tracks = tracks
        self.tick_duration = iter(tick_duration)

    def play(self):
        for track in self.tracks:
            track.step()
        try:
            threading.Timer(next(self.tick_duration), self.play).start()
        except StopIteration:
            return


# if __name__ == '__main__':
#     test_score = {
#         'notes': [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1],
#         'duration': [1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1],
#     }
#
#     play_func = {}
#     for i in range(22):
#         play_func[i] = functools.partial(print, i)
#
#     p1 = Track(test_score, play_func)
#     p2 = Track(test_score, play_func)
