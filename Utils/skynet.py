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
from Core import Parser as pars
from LowLevel import LowLevel as LL
from LowLevel import DB

bot = telegram_chatbot("Files/config.cfg")


def skynetWriteBan(userID, userName, firstName, lastName, admin):
    if LL.skynetStatus() == True:
        name = firstName + " " + lastName
        post = {"UserID": userID, "UserName": userName,
                "Name": name, "Admin": admin}
        DB.writeDB(post)
        sBanSuccess = True
        return sBanSuccess
    elif LL.skynetStatus() == False:
        sBanSuccess = False
        return sBanSuccess


def skynetCheck(userID):
    userOnBanList = False

    if LL.skynetStatus() == True:
        foo = DB.readDB("UserID", userID)
        if foo == True:
            userOnBanList = True
        else:
            userOnBanList = False
    return userOnBanList


def skynetBan(chatID, userID, firstname):
    bot.kick_chat_member(chatID, userID, until=0)
    reply = pars.LoadDialog("skynetBan", "admin_commands")
    reply = reply.fromat(firstname)
    return reply
