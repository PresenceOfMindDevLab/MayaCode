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

from Utils import Logger as Log
from LowLevel import LowLevel as LL

class loadParser():
    def LoadDialog(self, msg, branch):
        reply = None
        with open("Core/Data/json/Dialogs.json") as dialogs:
            data = json.load(dialogs)
            reply = data[branch][msg]
            return reply

class readParser():
    def ReadTrigger(self, msg):
        branch = None
        with open("Core/Data/json/trigger.json") as trigger:
            data = json.load(trigger)
            equals = data["equals"]
            inter = data["interactions"]

            if msg in equals:
                branch = "equals"
                msg = msg
                return msg, branch

            else:
                if msg.split(" ")[0] == "maya" or msg.split(" ")[0] == "Maya":
                    msg = msg.split(' ', 1)[1]
                    
                    if msg in inter:
                        branch = "interactions"
                        msg = msg
                        return msg, branch

                    else:
                        branch = None
                        return msg, branch

                else:
                    branch = None
                    return msg, branch


    def ReadReply(self, msg):
        branch = None
        with open("Core/Data/json/trigger.json") as trigger:
            data = json.load(trigger)
            sinter = data["simple_interactions"]
            uinter = data["user_interactions"]
            admin = data["admin_commands"]

            if msg in sinter:
                branch = "simple_interactions"
                msg = msg
                return msg, branch

            if msg in admin:                 #! change this
                branch = "admin_commands"
                msg = msg
                return msg, branch

            if msg.split(" ")[0] == "maya" or msg.split(" ")[0] == "Maya":
                msg = msg.split(' ', 1)[1]

                if msg in uinter:
                    branch = "user_interactions"
                    msg = msg
                    return msg, branch

            else:
                branch = None
                return msg, branch

class yaml_config_parser():
    def __init__(self):
        print("test")

    def ReadSettings(self, section, segment, items):
        with open("Core/Data/yaml/Settings.yaml","r") as setting:
            data = yaml.full_load(setting)
            try:
                info = data[section][segment][items]
            except:
                data = None
            print("Settings: " + str(info))
            return info

class fileParser():

    def ReadSticker(self, pack, sticker):
        with open("Core/Data/json/sticker.json") as stk:
            data = json.load(stk)
            stk = data[pack][sticker]
            return stk

class parserMod():
    
    def Usage(self, branch):
        with open("Core/Data/json/trigger_usage.json") as use:
            data = json.load(use)
        
        count = data[branch]["count"]
        count = int(count) + 1
        Log.d("Used " + branch + " " + str(count) + " times!")
        data[branch]["count"] = count

        with open("Core/Data/json/trigger_usage.json", "w") as use:
            json.dump(data, use, indent=4)

    def getWarnUser(self,chat_id, user_id):
        with open("Core/Data/json/warnings.json")as warn:
            data = json.load(warn)

            try:
                warnings = data[chat_id][user_id]["warnings"]
                count, item = LL.warnUser(warnings)
                data[chat_id][user_id]["warnings"] = count

                with open("Core/Data/json/warnings.json", "w") as warn:
                    if count == 3:
                        del data[chat_id][user_id]
                        warn.write[json.dumps(data, warn, indent=4)]
                        warn.close()

                    json.dump(data, warn, indent=4)
                    warn.close()

            except:
                warnings = None
                count, item = LL.warnUser(0)
                data[chat_id][user_id]["warnings"] = count

                with open("Core/Data/json/warnings.json", "w") as warn:
                    warn.write[json.dump(data, warn, indent=4)]
                    warn.close()

            return count, item #! ändern