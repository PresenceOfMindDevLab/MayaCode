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
from Core.MayaChan import telegram_chatbot
from Core.Parser import yaml_config_parser
from Utils import Logger as Log

from pythonping import ping
import time
import yaml

bot = telegram_chatbot("Files/config.cfg")
pars = yaml_config_parser()

def uptime():
    uptime = time.time() - Base.startTime
    uptime = time.strftime("%H:%M:%S", time.gmtime(uptime))
    return uptime

def pingt():
    print(pars.ReadSettings("LowLevel","ping","ping_ip"))
    response_list = ping(pars.ReadSettings("LowLevel","ping","ping_ip"), size=40, count=1)
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

def skynetStatus():
    skynet = None
    try:
        skynet = pars.ReadSettings("Utils", "Skynet", "enabled")
    except:
        skynet = None
    
    return skynet

def getAdmins(chat_id, user_id, from_id):
    command = False
    reply = None
    adminAr = bot.get_chat_administrators(chat_id)
    adminAr = adminAr["result"]
    Log.d("Get Group Admins")
    if adminAr:
        i = 0
        admin = False
        from_admin = False
        while admin != True:
            try:
                admin_id = str(adminAr[i]["user"]["id"])
                if int(user_id) != int(admin_id):
                    i = i +1
                else:
                    admin = True
                    
            except:
                admin_id = None
                break
        pass
        i = 0
        while from_admin != True:
            try:
                admin_id = str(adminAr[i]["user"]["id"])
                if int(from_id) != int(admin_id):
                    i = i +1
                else:
                    from_admin = True
                    
            except:
                from_id = None
                break
        pass
        if admin == True:
            reply = "Sorry... I can't do this to an admin"
        if from_admin == False:
            reply = "Only admins can do that!"
        if admin != True and from_admin != False:
            command = True
        else:
            command = False
        print("LLAdmin: " + str(reply) + " " + str(command))
        return reply, command

def warnUser(warnings):
    warnings = int(warnings) + 1
    item = "warn" + str(warnings)
    return warnings, item


#! return dont work... occurred in ping and uptime