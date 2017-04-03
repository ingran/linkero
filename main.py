# -*- coding: utf-8 -*-

# 1) Linkero Core
import core.linkero as linkero
#import core.gateway.gevent_service as gevent
#import core.gateway.waitress_service as waitress

# 2) APIs developed to use with Linkero
import examples.testAPI

# 3) Load desired APIs
examples.testAPI.loadTestAPI()

# 4) Run Linkero
linkero.run()
