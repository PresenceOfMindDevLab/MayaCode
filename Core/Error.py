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

class MayaError(Exception):
    def __init__(self, x):
        self.message = x

    def __str__(self):
        return self.message

class Unauthorized(MayaError):
    def __init__(self):
        self.message = "Not autorized"

class InvalidKickTime(MayaError):
    def __init__(self, until):
        super(InvalidKickTime, self).__init__("%s is not allowed" % until)

class NoQuotedMessage(MayaError):
    def __init__(self):
        self.message = "Not quoted"

class NotEnoughtRights(MayaError):
    def __init__(self):
        self.message = "Bot has no permission for that."

class ServerError(Exception):
    def __init__(self, message):
        super(ServerError, self).__init__()
        self.message = message

    def __str__(self):
        return '%s' % self.message

class TelegramError(Exception):
    def __init__(self, message):
        super(TelegramError, self).__init__()
        self.message = message

    def __str__(self):
        return '%s' % self.message

class UnknownError(MayaError):
    def __init__(self, value):
        self.message = "Unknown error: %s" % value

class BadRequest(MayaError):
    def __init__(self, desc):
        self.message = "%s" % desc

class NotFound404(MayaError):
    def __init__(self):
        self.message = "The requested resource was not found."