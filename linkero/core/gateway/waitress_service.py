# -*- coding: utf-8 -*-

import linkero.core.linkero as linkero
from waitress import serve
import os


def run(app):
    linkero.printWellcome()
    linkero.createDB()
    serve(app, host=linkero.config["host"]["ip"], port=int(os.environ.get('PORT', linkero.config["host"]["port"])),
          threads=linkero.config["waitress"]["threads"], connection_limit=linkero.config["waitress"]["spawn"])