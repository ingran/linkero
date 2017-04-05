# -*- coding: utf-8 -*-

import core.linkero as linkero
from waitress import serve

def run(app):
    linkero.printWellcome()
    linkero.createDB()
    serve(app, host=linkero.config["host"]["ip"], port=linkero.config["host"]["port"],
          threads=linkero.config["waitress"]["threads"], connection_limit=linkero.config["waitress"]["spawn"])