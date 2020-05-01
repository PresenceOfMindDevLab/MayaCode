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

from Core.MayaChan import telegram_chatbot as bot
from Utils import LowLevel as LL
from Core import Parser as pars
from Utils import Logger as Log


class maya_trigger:
    
    def make_reply(self, msg, username, first_name):
        reply = None

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
            
#            if "{}" in reply and branch == "interactions":
#                reply = reply.format(username)

            return reply



class maya_reply_usermessage:

    def reply_to_usermessage(self, msg, sendname, takename, chat_id, user_id):
        reply = None
        Log.d("Running RTU")
        Log.d(msg + sendname + takename + str(chat_id) + str(user_id))
        if msg is not None:
            
            msg, branch = pars.ReadReply(msg)
            Log.d(msg + " " + branch)
            try:
                if branch == "admin_commands":
                    admin = LL.getAdmins(chat_id, user_id)
                    Log.d(admin)
                    if admin == True:
                        reply = "Sorry... I can't do this to an admin"
                    if admin == False:
                        if msg == "ban":
                            Log.d("ban function")
                            bot.kick_chat_member(chat_id, user_id, until=0)
                            stk = pars.ReadSticker("manomp", "ban")
                            bot.send_sticker(chat_id, stk)
                            reply = pars.LoadDialog(msg, branch)
                            reply = reply.format(takename)
                            return reply

            
                if branch == "simple_interactions":
                    Log.d(branch)
                    if takename == "MayaChan":
                        reply = pars.LoadDialog(msg, branch)
                        Log.d(reply)
                        pars.Usage(branch)
                        return reply
            except:
                branch = None
    
            return reply

#                if user_id in admins:
#                    reply = "Sorry... I can't ban an admin"
#                    return reply --> add exception later
                
                


            #if str("{}") in reply:
            #    reply = reply.format(takename)
            