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
import os
import json
import configparser as cfg
import time

from Utils import Logger as Log
from Core.Error import InvalidKickTime, Unauthorized, NoQuotedMessage, UnkownError, NotEnoughtRights, BadRequest, NotFound404

bans = {"h12": 43200, "h10": 36000, "h8": 28800, "h4": 14400, "h2": 7200, "h1": 3600, "h0": 1800, "ever": 0}

class telegram_chatbot():
    def __init__(self, config):
        self.token = self.ReadTokenFromConfig(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
        self.masterID = self.ReadMasterID(config)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=10&limit=None"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id, parse_mode=None):
        url = self.base + "sendMessage?chat_id={}&text={}&parse_mode={}".format(chat_id, msg, parse_mode)
        if msg is not None:
            value = requests.get(url)
            self.getError(value)

    def kick_chat_member(self, chat_id, user_id, until=None):
        if until:
            if until not in bans:
                Log.d("Invalid kick time")
                raise InvalidKickTime(until)

            until = time.time() + bans[until]
        url = self.base +"kickChatMember?chat_id={}&user_id={}&until_date={}".format(chat_id, user_id, until)
        value = requests.get(url)
        self.getError(value)

    def get_chat_administrators(self, chat_id):
        url = self.base +"getChatAdministrators?chat_id={}".format(chat_id)
        admins = requests.get(url)
        return json.loads(admins.content)

    def send_sticker(self, chat_id, sticker=None, repyl_to_message_id=None):
        url = self.base + "sendSticker?sticker={}&chat_id={}&reply_to_message_id={}".format(sticker, chat_id, repyl_to_message_id)
        value = requests.get(url)
        self.getError(value)

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

    def readDBData(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        username = parser.get('db', 'username')
        pw = parser.get('db', 'pw')
        return username, pw

    def getError(self, value):
        if value.status_code != 200:
            if "rights" in value.json()["description"]:
                raise NotEnoughtRights

            if value.status_code == 403 or "Unauthorized" in value.json()["description"]:
                raise Unauthorized

            if value.status_code == 400:
                raise BadRequest(value.json()["description"] + " :(")

            if value.status_code == 404:
                raise NotFound404

            else:
                raise UnkownError(value.json()["description"])