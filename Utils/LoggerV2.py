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

from Core import Parser as pars


def logV2Activation():

    try:
        LogV2 = pars.ReadSettings("Logging", "LoggerV2", "enabled")
    except:
        LogV2 = None

    try:
        LogV2T1 = pars.ReadSettings("Logging", "LoggerV2", "T1")
    except:
        LogV2T1 = None
    try:
        LogV2T2 = pars.ReadSettings("Logging", "LoggerV2", "T2")
    except:
        LogV2T2 = None
    data = LogV2, LogV2T1, LogV2T2

    return data


def crt():
    return time.strftime("%H:%M:%S")


# * check every API return for error codes
