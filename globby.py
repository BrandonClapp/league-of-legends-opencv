from PIL import Image


subs_confidence = []


def sub_confidence(cb):
    subs_confidence.append(cb)


def set_confidence(value):
    global confidence
    confidence = value
    for s in subs_confidence:
        s(confidence)


def init():
    global image
    image = Image.new("RGB", (350, 350), (0, 255, 255))

    global closing
    closing = False

    global champion_name
    champion_name = 'Udyr'

    global confidence
    confidence = 0.5
