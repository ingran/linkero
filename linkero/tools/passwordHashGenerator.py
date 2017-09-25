# -*- coding: utf-8 -*-

import sys
import getpass
from linkero.core.common import bcolors
from passlib.apps import custom_app_context as pwd_context

def generatePasswordHash():

    if (sys.version_info > (3, 0)):
        password = input("\nType the password: ")
    else:
        password = raw_input("\nType the password: ")

    password_hash = pwd_context.encrypt(password)

    print("\n"+bcolors.OKBLUE+password_hash+bcolors.ENDC+"\n")

    print(bcolors.WARNING+"Copy the generated password hash in "+bcolors.OKBLUE
        +"adminSecret"+bcolors.WARNING+" param inside of the config.json file"+bcolors.ENDC)



