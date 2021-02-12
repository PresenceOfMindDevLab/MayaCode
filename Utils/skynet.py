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

from Core.MayaChan import telegram_chatbot
from Core.Parser import loadParser as loadPars
from LowLevel import LowLevel as LL
from LowLevel import DB

bot = telegram_chatbot("Files/config.cfg")

class skynet():
    def __init__(self):
        self.status = LL.skynetStatus()

    def skynetWriteBan(self, userID, userName, firstName, lastName, admin):
        if self.status == True:
            name = firstName + " " + lastName
            post = {"UserID": userID, "UserName": userName, "Name": name, "Admin": admin}
            DB.writeDB(post)

    def skynetBan(self, chatID, userID, firstname):
        bot.kick_chat_member(chatID, userID, until=0)
        reply = loadPars.LoadDialog("skynetBan", "admin_commands")
        reply = reply.fromat(firstname)
        return reply

class skynetUtils():
    def __init__(self):
        self.status = LL.skynetStatus()

    def skynetCheck(self, userID):
        userOnBanList = False

        if self.status == True:
            foo = DB.readDB("UserID", userID)
            if foo == True:
                userOnBanList = True
        else:
            userOnBanList = False
        return userOnBanList