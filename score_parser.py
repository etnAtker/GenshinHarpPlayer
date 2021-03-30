def parse(score):
    min_tick = 16
    a_tempo = 4

    pitch_map = {'_': 0, '-': 7, '^': 14}
    pri_score = {'notes': [], 'duration': []}
    tick_duration = []

    parsing = 'notes'
    bpm = 60
    for token in score:
        if token == 'dur':
            parsing = 'duration'
        elif token[0] == 'b':
            bpm = int(token[1:])
        else:
            if parsing == 'notes':
                pri_score['notes'].append(int(token[0]) + pitch_map[token[1]])
            else:
                pri_score['duration'].append(min_tick / int(token))
                tick_duration += [60 / bpm / (min_tick / a_tempo)] * int(min_tick / int(token))

    return pri_score, tick_duration


# if __name__ == '__main__':
#     with open('score.txt', 'r') as f:
#         score_txt = f.read()
#
#     print(parse(score_txt.split()))
