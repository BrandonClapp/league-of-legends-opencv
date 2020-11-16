SAVE = 'SAVE'

subs = {
    'SAVE': []
}


def dispatch(id, payload):
    for s in subs[id]:
        s(payload)


def subscribe(id, cb):
    subs[id].append(cb)
