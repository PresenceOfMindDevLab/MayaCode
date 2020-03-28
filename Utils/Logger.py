# coding=utf-8

# Copyright (c) 2020 HartiChan

# 888b     d888                                    .d8888b.                888          
# 8888b   d8888                                   d88P  Y88b               888          
# 88888b.d88888                                   888    888               888          
# 888Y88888P888  8888b.  888  888  8888b.         888         .d88b.   .d88888  .d88b.  
# 888 Y888P 888     "88b 888  888     "88b        888        d88""88b d88" 888 d8P  Y8b 
# 888  Y8P  888 .d888888 888  888 .d888888 888888 888    888 888  888 888  888 88888888 
# 888   "   888 888  888 Y88b 888 888  888        Y88b  d88P Y88..88P Y88b 888 Y8b.     
# 888       888 "Y888888  "Y88888 "Y888888         "Y8888P"   "Y88P"   "Y88888  "Y8888  
#                             888                                                       
#                        Y8b d88P                                                       
#                         "Y88P"    

import inspect
import time

def time():
    return time.strftime("%H:%M:%S")

def call_elaborator(caller_foo):
    return caller_foo + (14 - len(caller_foo)) * " "

def printl(type, lmsg, foo):
    text = "[ %s ] %s - [from: %s ] - %s" % (type, time(), foo, lmsg)
    with open("Files/log.txt", "a") as fl:
        fl.write(text + "\n")
    print(text)
    return True

def printe(text):
    with open("Files/error.txt", "a") as fl:
        fl.write(text + "\n")
        fl.close()
    print(text)

def d(text):
    printl("Debug ", text, call_elaborator(inspect.stack()[1][3]))


def i(text):
    printl("Info  ", text, call_elaborator(inspect.stack()[1][3]))


def a(text):
    printl("Action", text, call_elaborator(inspect.stack()[1][3]))


def w(text):
    printl("Warn  ", text, call_elaborator(inspect.stack()[1][3]))

def e(text):
    text = str(text)
    printe("[ Error  ] %s - [from: %s] - Error: %s line: ~%s" % (time(), call_elaborator(inspect.stack()[1][3]), text,
                                                                inspect.getframeinfo(inspect.stack()[1][0]).lineno))
    return False

def critical(text, shutdown=True):
    text = str(text)
    printe("[CRITICAL] %s - [from: %s] - Error critical: %s line: ~%s" % (time(), call_elaborator(inspect.stack()[1][3]), text,
                                                                        inspect.getframeinfo(
                                                                            inspect.stack()[1][0]).lineno))
    if shutdown:
        exit()