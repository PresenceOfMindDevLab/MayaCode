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
from Core import Parser as pars
from Utils import Logger as Log
from Core import Manager as Manage

bot = telegram_chatbot("Files/config.cfg")


class maya_trigger:
    
    def make_reply(self, msg, username, first_name):
        reply = None
        parse_mode = None
        if msg is not None:
            msg, branch = pars.ReadTrigger(msg)
            print(str(msg) + str(branch)) #!
            reply, parse_mode =  Manage.trigger(msg, branch, username)
            #Log.i(str(reply) + " " + str(parse_mode))
        return reply, parse_mode

class maya_reply_usermessage:

    def reply_to_usermessage(self, msg, sendname, takefirstname, takelastname, chat_id, from_id, user_id, takeusername):
        reply = None
        Log.d("Running RTU")
        if msg is not None:
            
            msg, branch = pars.ReadReply(msg)
            try:
                if branch == "admin_commands":
                    reply = Manage.admin_commands(msg, chat_id, from_id, user_id, takefirstname, branch, takelastname, sendname, takeusername)
                    return reply
            
                if branch == "simple_interactions":
                    if takefirstname == "MayaChan":
                        reply = pars.LoadDialog(msg, branch)
                        pars.Usage(branch)
                        return reply

                if branch == "user_interactions":
                    reply = pars.LoadDialog(msg, branch)
                    pars.Usage(branch)
                    
            except:
                branch = None
            if reply is not None:
                if "{}" in reply:
                    reply = reply.format(takefirstname)
        return reply