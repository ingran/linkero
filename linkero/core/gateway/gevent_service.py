# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
from gevent.wsgi import WSGIServer
from gevent.pool import Pool

def run(app):
    linkero.printWellcome()
    linkero.createDB()
    if linkero.config["SSL"]["activate"]:
        gevert_server = WSGIServer((linkero.config["host"]["ip"], linkero.config["host"]["port"]), app,
                                   spawn=Pool(linkero.config["gevent"]["spawn"]),
                                   log='default' if (linkero.config["gevent"]["accessLog"] == True) else None,
                                   keyfile=linkero.config["SSL"]["key"], certfile=linkero.config["SSL"]["certificate"])
    else:
        gevert_server = WSGIServer((linkero.config["host"]["ip"], linkero.config["host"]["port"]), app,
                                   log='default' if (linkero.config["gevent"]["accessLog"] == True) else None,
                                   spawn=Pool(linkero.config["gevent"]["spawn"]))
    gevert_server.serve_forever()