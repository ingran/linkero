# -*- coding: utf-8 -*-

from tools.passwordHashGenerator import generatePasswordHash
from core.common import bcolors
from submodules.SimplePythonTools.common import askFor

def switch(x):
    return {
        0: exec_exit,
        1: exec_passwordHashGenerator
    }.get(x, exec_exit) # default if x not found

def exec_passwordHashGenerator():
    generatePasswordHash()
def exec_exit():
    exit()

def printInstructions():
    print("\nType desired option number and press enter.\nType "+bcolors.FAIL+"-1"+bcolors.ENDC+" to forced exit.\n")


def printOptions():
    print(bcolors.WARNING + "\n0) " + bcolors.ENDC + "Exit")
    print(bcolors.WARNING+"1) "+bcolors.ENDC+ "Password Hash Generator")

printOptions()
printInstructions()
option_selected = askFor("Selected option: ", 2)
switch(option_selected)()