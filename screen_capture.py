import cv2 as cv
import numpy as np
from time import perf_counter
from time import sleep
from PIL import ImageGrab, Image
import champ_list
import globby
import ui_events
import audio_player

current_champion = ''
current_confidence = 0.5


def calculate_spot(x, y):
    if x < y and x < (350 - y):
        audio_player.play('top-left')
    elif x < y and x > (350 - y):
        audio_player.play('bottom-left')
    elif x > y and x > (350 - y):
        audio_player.play('bottom-right')
    elif x > y and x < (350 - y):
        audio_player.play('top-right')


def change_champion():
    setting = champ_list.get_champion(globby.champion_name)
    image = setting.image

    cvChamp = cv.imread(f'champions/{image}.png')
    cvChamp = cv.resize(cvChamp, (28, 28), interpolation=cv.INTER_AREA)
    cvChamp = cvChamp[5:23, 5:23]
    global current_champion
    current_champion = globby.champion_name

    global current_confidence
    current_confidence = (setting.confidence)
    globby.set_confidence(current_confidence)

    return (cvChamp, setting)


def on_confidence_updated(c):
    global current_confidence
    current_confidence = c


def on_ui_save(confidence):
    champ_list.save_setting(current_champion, confidence)


def start_capture():
    global current_champion
    current_champion = globby.champion_name

    global current_confidence
    current_confidence = globby.confidence

    (cvChamp, setting) = change_champion()

    globby.sub_confidence(on_confidence_updated)
    ui_events.subscribe(ui_events.SAVE, on_ui_save)

    while True:

        if current_champion != globby.champion_name:
            (cvChamp, setting) = change_champion()

        w = 1920
        h = 1080

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

        if globby.closing:
            break

        img = ImageGrab.grab(bbox=(w-350, h-350, w, h))  # x, y, w, h
        img_np = np.array(img)
        mm = cv.cvtColor(img_np, cv.COLOR_RGBA2BGR)

        result = cv.matchTemplate(cvChamp, mm, cv.TM_SQDIFF_NORMED)
        mn, _, mnLoc, _ = cv.minMaxLoc(result)
        confidence = 1-mn

        rect_color = (0, 255, 0)
        if confidence > current_confidence:
            MPx, MPy = mnLoc
            trows, tcols = cvChamp.shape[:2]
            # print((MPx, MPy), MPy - MPx)
            calculate_spot(MPx, MPy)
            cv.rectangle(mm, (MPx, MPy), (MPx+tcols, MPy+trows), rect_color, 2)

        rgb_mm = cv.cvtColor(mm, cv.COLOR_BGR2RGBA)
        pilImg = Image.fromarray(rgb_mm)

        globby.image = pilImg

    cv.destroyAllWindows()
