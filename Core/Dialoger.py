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

bot = telegram_chatbot("Files/config.cfg")


class maya_trigger:
    
    def make_reply(self, msg, username, first_name):
        reply = None
        parse_mode = None
        # check for equals and inter

        if msg is not None:
            
            msg, branch = pars.ReadTrigger(msg)

            try: 
                reply = str(pars.LoadDialog(msg, branch))
                pars.Usage(branch)

            except:
                branch = None
            
            if msg == "ping":
                pingr = LL.pingt()
                reply = reply.format(pingr)
                
            if msg == "info":
                reply = reply.format(LL.uptime(), LL.pingt())
                parse_mode = "markdown"

            if branch == "interactions":
                if "{}" in reply:
                    reply = reply.format(username)

            return reply, parse_mode



class maya_reply_usermessage:

    def reply_to_usermessage(self, msg, sendname, takename, chat_id, user_id):
        reply = None
        Log.d("Running RTU")
        if msg is not None:
            
            msg, branch = pars.ReadReply(msg)
            try:
                if branch == "admin_commands":
                    admin = LL.getAdmins(chat_id, user_id)
                    if admin == True:
                        reply = "Sorry... I can't do this to an admin"
                    if admin == False:
                        if msg == "ban":
                            reply = pars.LoadDialog(msg, branch)
                            reply = reply.format(takename)
                            bot.kick_chat_member(chat_id, user_id, until=0)
                            stk = pars.ReadSticker("manomp", "ban")
                            bot.send_sticker(chat_id, stk)
                            return reply

            
                if branch == "simple_interactions":
                    if takename == "MayaChan":
                        reply = pars.LoadDialog(msg, branch)
                        pars.Usage(branch)
                        return reply

                if branch == "user_interactions":
                    reply = pars.LoadDialog(msg, branch)
                    pars.Usage(branch)
                    
            except:
                branch = None
            if "{}" in reply:
                reply = reply.format(takename)
            return reply