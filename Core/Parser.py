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

import requests
import json
import yaml

def ReadTrigger(msg):
    jsonDialog = None
    with open("Core/Data/json/trigger.json") as trigger:
        data = json.load(trigger)
        equals = data["equals"]
        inter = data["interactions"]

        if msg in equals:
            jsonDialog = "equals"
            msg = msg
            return msg, jsonDialog

        else:
            if msg.split(" ")[0] == "maya" or msg.split(" ")[0] == " Maya":
                msg = msg.split(' ', 1)[1]
                if msg in inter:
                    jsonDialog = "interactions"
                    msg = msg
                    return msg, jsonDialog
                else:
                    jsonDialog = None
                    return msg, jsonDialog
            else:
                jsonDialog = None
                return msg, jsonDialog


def ReadReply(msg):
    jsonDialog = None
    with open("Core/Data/json/trigger.json") as trigger:
        data = json.load(trigger)
        sinter = data["simple_interactions"]
        if msg in sinter:
            jsonDialog = "simple_interactions"
            msg = msg
            return msg, jsonDialog
        else:
            jsonDialog = None
            return msg, jsonDialog

def LoadDialog(msg, jsonDialog):
    reply = None
    with open("Core/Data/json/Dialogs.json") as dialogs:
        data = json.load(dialogs)
        reply = data[jsonDialog][msg]
        return reply


def Usage(jsonDialog):
    with open("Core/Data/json/trigger_usage.json") as usage:
        data = json.load(usage)
        count = data[jsonDialog]
        count = count + 1
        rep = data[jsonDialog][count]
        json.dump(rep, usage)

def ReadSettings(section, segment, items):
    with open("Core/Data/yaml/Settings.yaml","r") as setting:
        data = yaml.full_load(setting)
        try:
            info = data[section][segment][items]
        except:
            data = None
        return info
