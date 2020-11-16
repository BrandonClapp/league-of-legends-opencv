import os
import winsound
import time

LAST_PLAYED = None
LAST_POSITION = None


def play(position):
    global LAST_PLAYED
    global LAST_POSITION

    if LAST_PLAYED is None:
        LAST_PLAYED = time.time()

    if time.time() - LAST_PLAYED > 10 or LAST_POSITION != position:
        winsound.PlaySound('audio/' + position,
                           winsound.SND_FILENAME | winsound.SND_ASYNC)
        LAST_PLAYED = time.time()
        LAST_POSITION = position


if __name__ == '__main__':
    play('audio/top-left')
