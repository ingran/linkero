# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
from gevent.wsgi import WSGIServer
from gevent.pool import Pool
import os


def run(app):
    linkero.printWellcome()
    linkero.createDB()
    if linkero.config["SSL"]["activate"]:
        gevent_server = WSGIServer((linkero.config["host"]["ip"],
                                    int(os.environ.get('PORT', linkero.config["host"]["port"]))),
                                    app, spawn=Pool(linkero.config["gevent"]["spawn"]),
                                    log='default' if (linkero.config["gevent"]["accessLog"] == True) else None,
                                    keyfile=linkero.config["SSL"]["key"], certfile=linkero.config["SSL"]["certificate"])
    else:
        gevent_server = WSGIServer((linkero.config["host"]["ip"],
                                    int(os.environ.get('PORT', linkero.config["host"]["port"]))),
                                    app, spawn=Pool(linkero.config["gevent"]["spawn"]),
                                    log = 'default' if (linkero.config["gevent"]["accessLog"] == True) else None)
    gevent_server.serve_forever()