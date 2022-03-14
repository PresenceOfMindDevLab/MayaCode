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
# import operator
# import re
import time
# import random
# import sys
# import psutil
# import json

from Core.MayaChan import telegram_chatbot
from Core import Parser as pars
from Utils import Logger as Log
from Core.Dialoger import maya_trigger, maya_reply_usermessage
from Utils import skynet


bot = telegram_chatbot("Files/config.cfg")
trigger = maya_trigger()
repum = maya_reply_usermessage()
startTime = time.time()
Log.d("Set start time: " + str(time.strftime("%H:%M:%S", time.gmtime(startTime))))


def MayaRun():

    update_id = None
    Log.d("Run Maya")
    while True:

        updates = bot.get_updates(offset=update_id)
        updates = updates["result"]
        print(updates)
        print(update_id)

        if updates:

            for item in updates:

                update_id = item["update_id"]
                try:

                    message = str(item["message"]["text"])

                except:

                    message = None
                try:
                    # ? error with edited message
                    from_ = item["message"]["from"]["id"]
                except:
                    from_ = None
                try:
                    chat_ = item["message"]["chat"]["id"]
                except:
                    chat_ = None
                try:
                    first_name_ = item["message"]["from"]["first_name"]
                except:
                    first_name_ = None

                try:
                    username_ = item["message"]["from"]["username"]
                except:
                    username_ = None

                try:
                    last_name_ = item["message"]["from"]["last_Name"]
                except:
                    last_name_ = None

                try:
                    chat_name_ = item["message"]["chat"]["title"]
                except:
                    chat_name_ = None

                try:
                    new_chat_member_ = item["message"]["new_chat_participant"]
                except:
                    new_chat_member_ = None

                try:
                    gone_chat_member_ = item["message"]["left_chat_member"]
                except:
                    gone_chat_member_ = None

                Log.i(from_)
                Log.i(chat_)

                if new_chat_member_ is not None:

                    new_chat_member_id_ = item["message"]["new_chat_participant"]["id"]
                    new_chat_member_first_name_ = item["message"]["new_chat_participant"]["first_name"]
                    #! Add Skynet function
                    UTS = skynet.skynetCheck(new_chat_member_id_)

                    if UTS == True:

                        reply = skynet.skynetBan(
                            chat_, new_chat_member_id_, new_chat_member_first_name_)
                        bot.send_message(reply, chat_)

                    if UTS == False:

                        new_chat_member_name_ = item["message"]["new_chat_participant"]["first_name"]
                        Log.a("welcome")
                        reply = "Welcome " + new_chat_member_name_ + " to " + chat_name_ + " ^^"
                        bot.send_message(reply, chat_)
                        stk = pars.ReadSticker("manomp", "welcome")
                        bot.send_sticker(chat_, stk)

                if gone_chat_member_ is not None:

                    gone_chat_member_name_ = item["message"]["left_chat_member"]["first_name"]
                    Log.a("Left")
                    reply = "Goodbye " + gone_chat_member_name_
                    if from_ == "MayaChan":
                        bot.send_message(reply, chat_)

                try:
                    reply_to_message_ = item["message"]["reply_to_message"]
                except:
                    reply_to_message_ = None

                if reply_to_message_ is not None:

                    reply_to_message_first_name_ = item["message"]["reply_to_message"]["from"]["first_name"]
                    try:
                        reply_to_message_last_name_ = item["message"]["reply_to_message"]["from"]["last_name"]
                    except:
                        reply_to_message_last_name_ = None
                    try:
                        reply_to_message_username_ = item["message"]["reply_to_message"]["from"]["username"]
                    except:
                        reply_to_message_username_ = None

                    reply_id_ = item["message"]["reply_to_message"]["from"]["id"]
                    reply = repum.reply_to_usermessage(message, first_name_, reply_to_message_first_name_,
                                                       reply_to_message_last_name_, chat_, from_, reply_id_, reply_to_message_username_)
                    bot.send_message(reply, chat_)

                if reply_to_message_ is None:

                    if from_ == chat_:
                        reply, parse_mode = trigger.make_reply(
                            message, username_, first_name_)
                        bot.send_message(reply, from_, parse_mode)

                    if from_ != chat_:
                        reply, parse_mode = trigger.make_reply(
                            message, username_, first_name_)
                        Log.d(str(reply) + " " + str(parse_mode))
                        bot.send_message(reply, chat_, parse_mode)


def idle():
    while True:
        Log.d("Run Idle")
        time.sleep(10)

# ToDo
# make query for equals and interactions

# --> like "ping" and "Maya do this" (BotName + Command)

# make new interaction to take the "take_name" (like maya kill him)
# --> and username interactions to ping user
