import datetime

from connexion import NoContent

reles = [
    {'id': 1, 'status': True, 'gpio':14},
    {'id': 2, 'status': False, 'gpio':14},
    {'id': 3, 'status': False, 'gpio':14},
    {'id': 4, 'status': False, 'gpio':14},
]


def put(releID):
    status = False
    change = False
    for r in reles:
        if r['id'] == int(releID):
            r['status'] = not r['status']
            status = r['status']
            change = True
    rele = {}
    rele['id'] = releID
    rele['last_updated'] = datetime.datetime.now()
    rele['status'] = status
    rele['change'] = change
    return rele, 201


def get(id):
    for r in reles:
        if r['id'] == id:
            return r,200
    return False,404


def search():
    return reles,200