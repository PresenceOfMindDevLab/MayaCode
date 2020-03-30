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
from Utils import LowLevel as LL
from Core import Parser as pars
from Utils import Logger as Log


class maya_trigger:
    
    def make_reply(self, msg, username, first_name):
        reply = None

        # check for equals and inter

        if msg is not None:
            
            msg, jsonDialog = pars.ReadTrigger(msg)

            try: 
                reply = pars.LoadDialog(msg, jsonDialog)

            except:
                jsonDialog = None
            
            if msg == "ping":
                ping = LL.pingt
                reply = reply % (ping)

            return reply



class yuko_reply_usermessage:
    
    def reply_to_usermessage(self, msg, sendname, takename):

        # check for sinter

        if msg is not None:
            
            msg, jsonDialog = pars.ReadReply(msg)

            try: 
                reply = pars.LoadDialog(msg, jsonDialog)
                
            except:
                jsonDialog = None
            reply = reply % (sendname)

            return reply