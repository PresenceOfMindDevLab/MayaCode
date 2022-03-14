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

import pymongo
from pymongo import MongoClient

from Core.MayaChan import telegram_chatbot
from LowLevel import LowLevel
from Utils import Logger as log

bot = telegram_chatbot("Files/config.cfg")


def dbConnect():

    username, pw = bot.readDBData("Files/config.cfg")
    cluster = MongoClient(
        "mongodb+srv://HartiChan:%s@einithi.pqidk.mongodb.net/%s?retryWrites=true&w=majority" % (pw, username))
    dbt = cluster.test
    log.d(dbt)

    db = cluster["MayaCode"]
    collection = db["Skynet"]
    return collection


def writeDB(post):

    collection = dbConnect()
    collection.insert_one(post)


def readDB(item, value):

    collection = dbConnect()
    if collection.count_documents({'UserID': 0}, limit=1) != 0:

        print("DB Bullshit")
        return False  # Change to true

    else:
        return False
