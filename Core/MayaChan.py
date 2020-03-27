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
import configparser as cfg

class telegram_chatbot():
    def __init__(self, config):
        self.token = self.ReadTokenFromConfig(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        self.masterID = self.ReadMasterID(config)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=10"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if msg is not None:
            requests.get(url)

    def sendbootmsg(self, bootmsg):
        url = self.base + "sendMessage?chat_id={}&text={}".format(self.masterID, bootmsg)
        requests.get(url)

    def ReadTokenFromConfig(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')
    
    def ReadMasterID(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'masterID')
