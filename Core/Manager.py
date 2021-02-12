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
from LowLevel import LowLevel as LL
from Core.Parser import loadParser as loadPars
from Core.Parser import readParser as readPars
from Core.Parser import fileParser as filePars
from Core.Parser import parserMod as modPars
from Utils import Logger as Log
from Utils import LoggerV2 as LogV2
from Utils import skynet

bot = telegram_chatbot("Files/config.cfg")

def trigger(msg, branch, username):
    reply = None
    parse_mode = None

    try: 
        reply = str(loadPars.LoadDialog(msg, branch))
        modPars.Usage(branch)

    except:
        branch = None
        return reply, parse_mode

    if msg == "ping":
        pingr = str(LL.pingt())
        print(pingr)
        reply = reply.format(pingr)
        return reply, parse_mode

    elif msg == "info":
        data = LogV2.logV2Activation()
        reply = reply.format(LL.uptime(), LL.pingt(), LL.skynetStatus(),data[0])  
        parse_mode = "markdown"
        return reply, parse_mode
    
    elif msg == "maya":
        reply = reply.format(username)
        return reply, parse_mode

    elif branch == "interactions":
        if "{}" in reply:
            reply = reply.format(username)
            return reply, parse_mode

    return reply, parse_mode

def admin_commands(msg, chat_id, from_id, user_id, takefirstname, branch, takelastname, admin, takeusername):
    reply = None
    reply, admin = LL.getAdmins(chat_id, user_id, from_id)

    if admin == True:
        if msg == "ban":
            skynet.skynetWriteBan(from_id, takeusername, takefirstname, takelastname, admin)
            reply = loadPars.LoadDialog(msg, branch)
            reply = reply.format(takefirstname)
            bot.kick_chat_member(chat_id, user_id, until=0)
            stk = filePars.ReadSticker("manomp", "ban")
            bot.send_sticker(chat_id, stk)
            return reply

        if msg == "warn":
            warns, item = modPars.getWarnUser(chat_id, user_id)
            reply = loadPars.LoadDialog(item, "lowLevel")
            if warns == 3:
                bot.kick_chat_member(chat_id, user_id, until=0)
                
    return reply