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
from Core import Base as Base
from Core import Parser as pars
from Utils import Logger as Log

from pythonping import ping
import time
import yaml

def uptime():
    uptime = time.time() - Base.startTime
    return uptime

def pingt():
    response_list = ping(pars.ReadSettings("LowLevel","ping","ping_ip"), size=1000, count=1)
    pingr = response_list.rtt_avg_ms
    Log.i("response time: " + str(pingr) + " ms")
    return pingr

def getAntispam():
    as_time = None
    Antispam = pars.ReadSettings("LowLevel","antispam", "antispam_enabled")
    try:
        as_time = pars.ReadSettings("LowLevel","antispam", "antispam_time")
    except:
        Antispam = False
    return as_time