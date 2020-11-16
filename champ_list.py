import json


class ChampionSettings:
    def __init__(self, image, confidence, calibrated):
        self.image = image
        self.confidence = confidence
        self.calibrated = calibrated


def get_setting(settings, name):
    spaced_name = name.replace(' ', '_')
    champ = settings['champions'][name]
    data = ChampionSettings(spaced_name + '_OriginalCircle',
                            champ['confidence'], champ['calibrated'])
    return data


def save_setting(champion, confidence):
    with open('settings.json', 'r+') as f:
        settings = json.load(f)
        settings['champions'][champion]['confidence'] = confidence
        settings['champions'][champion]['calibrated'] = True
        f.seek(0)
        f.truncate()
        json.dump(settings, f, indent=4)


def get_champion(name):
    with open('settings.json', 'r+') as f:
        settings = json.load(f)

        try:
            data = get_setting(settings, name)
        except KeyError:
            f.seek(0)
            f.truncate()
            settings['champions'][name] = {
                "confidence": 0.5, "calibrated": False
            }
            json.dump(settings, f, indent=4)
            data = get_setting(settings, name)
        print('dat', data)
        return data
