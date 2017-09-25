# -*- coding: utf-8 -*-

import threading
import os
from linkero.core.common import bcolors
from requests import post

# ++++++++++++++++++++++++++++++++++++++++++++++++++
# Delete current DB and generate new user demo:demo
# ++++++++++++++++++++++++++++++++++++++++++++++++++
if os.path.isfile('config/db.sqlite'):
    os.remove('config/db.sqlite')
def worker():
    post('http://localhost:5000/api/users', data={"username": "demo", "password": "demo", "secret": "admin"})
    print(bcolors.WARNING + "\nGranted access for user 'demo' with password 'demo'\n" + bcolors.ENDC)

t = threading.Timer(5, worker)  # Generate new user after 5 seconds
if os.path.isfile('config/config.json'):   # Thread only starts if config.json exists
    t.start()
# ++++++++++++++++++++++++++++++++++++++++++++++++++

# 1) Linkero Core
import linkero.core.linkero as linkero
import linkero.core.gateway.gevent_service as gevent
import linkero.core.gateway.waitress_service as waitress

# 2) APIs developed to use with Linkero
import testAPI

# 3) Load desired APIs
testAPI.loadTestAPI()

# 4) Run Linkero
linkero.run()  # Run with Werkzeug (not recommended for production environments)
#gevent.run(linkero.app)    # Run with Gevent
#waitress.run(linkero.app)   # Run with Waitress
