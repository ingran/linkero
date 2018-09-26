# -*- coding: utf-8 -*-

import logging
import json
import platform
import os
from shutil import copyfile
from .ascii import ascii_warning


class Metadata:
    def __init__(self):
        self.__version__ = '0.9.15'
        self.__author__ = 'Rubén de Celis Hernández'

    def get_version(self):
        return self.__version__
    def get_author(self):
        return self.__author__


def printWellcome():
    print(bcolors.HEADER+"")
    print("-----------------------------------------------------")
    print(bcolors.OKBLUE+"")
    print("  _____                                "+bcolors.WARNING+"|`-._/\_.-`|"+bcolors.OKBLUE)
    print(" |_   _|                               "+bcolors.WARNING+"|    ||    |"+bcolors.OKBLUE)
    print("   | |  _ __   __ _ _ __ __ _ _ __     "+bcolors.WARNING+"|___o()o___|"+bcolors.OKBLUE)
    print("   | | | '_ \ / _` | '__/ _` | '_ \    "+bcolors.WARNING+"|__((<>))__|"+bcolors.OKBLUE)
    print("  _| |_| | | | (_| | | | (_| | | | |   "+bcolors.WARNING+"\   o\/o   /"+bcolors.OKBLUE)
    print(" |_____|_| |_|\__, |_|  \__,_|_| |_|   "+bcolors.WARNING+" \   ||   / "+bcolors.OKBLUE)
    print("               __/ |                   "+bcolors.WARNING+"  \  ||  /  "+bcolors.OKBLUE)
    print("              |___/                    "+bcolors.WARNING+"   '.||.'   "+bcolors.OKBLUE)
    print(""+bcolors.ENDC)
    print("                                        Engineering  ")
    print(" v"+Metadata().get_version()+bcolors.HEADER+"")
    print("-----------------------------------------------------")
    print(""+bcolors.ENDC)

def loadMode():
    try:
        with open('config/config.json') as config_file:
            try:
                return json.load(config_file)["debug"]
            except KeyError:
                print(bcolors.WARNING+"Misformed config.json!"+bcolors.ENDC)
                exit()
    except IOError:
        print(bcolors.WARNING+"Error loading config.json!"+bcolors.ENDC)
        if not os.path.exists('config'):
            os.makedirs('config')
        copyfile(os.path.dirname(__file__)+'/../config/config.json', 'config/config.json')
        print(bcolors.WARNING+"\nDefault config.json generated! Try again."+bcolors.ENDC)
        exit()

def loadConfig(logger):
    print(bcolors.WARNING)

    if logger.getEffectiveLevel() != logging.DEBUG:
        logger.info("Running in Release Mode")
    else:
        logger.info("Running in Debug Mode")

    try:
        with open('config/config.json') as config_file:
            config = json.load(config_file)
            logger.info("Loaded: config/config.json")
    except IOError:
        print(bcolors.WARNING+"Error loading config.json!"+bcolors.ENDC)
        exit()

    print(bcolors.ENDC)
    return (config)

def setAccessLog(value):
    log = logging.getLogger('werkzeug')
    log.disabled = not value

def resolveRelativeWorkingDirectory(sqlite_path):
    if sqlite_path.find("///", 7) > 0 and sqlite_path.find("////", 7) == -1 and sqlite_path.find(":", 7) == -1:
        return sqlite_path.replace("///", ("///"+os.getcwd()+"/"), 1)

def checkDefaultAdminSecret(adminSecret):
    if adminSecret == "$5$rounds=549561$kWqFvPNTcBsl.Kle$ONikf.BJtqKKFTZbUtVmwZn0nDdwrsHhjyqgxRlUNw4":
        print(bcolors.WARNING + ascii_warning + bcolors.ENDC)
        print(bcolors.FAIL + "You are using 'admin' as admin secret\n" + bcolors.ENDC)
        print("Please generate new one with tools.passwordHashGenerator.generatePasswordHash()")
        print("You can call it typing the following command in your terminal:")
        print(bcolors.OKBLUE + "\n"
              "python -c 'from linkero.tools.passwordHashGenerator import generatePasswordHash; generatePasswordHash()'"
              + "\n" + bcolors.ENDC)

if os.name == 'nt' and platform.release() == '10' and platform.version() >= '10.0.14393':
    # Fix ANSI color in Windows 10 version 10.0.14393 (Windows Anniversary Update)
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
