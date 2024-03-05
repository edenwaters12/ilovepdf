# This module is part of https://github.com/edenwaters12/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 edenwaters12

file_name = "ILovePDF/plugins/dm/action_inline/__init__.py"

__author__ = "edenwaters12"
__email__ = "edenwaters12@gmail.com"
__telegram__ = "telegram.dog/edenwaters12"
__copyright__ = "Copyright 2021, edenwaters12"

iLovePDF = '''
  _   _                  ___  ___  ____ ™
 | | | |   _____ _____  | _ \|   \|  __| 
 | | | |__/ _ \ V / -_) |  _/| |) |  _|  
 |_| |___,\___/\_/\___| |_|  |___/|_|    
                         ❤ [Nabil A Navab] 
                         ❤ Email: edenwaters12@gmail.com
                         ❤ Telegram: @edenwaters12
'''

from plugins import *
from typing import Union
from lang import langList
from configs.log import log
from configs.db import myID
from libgenesis import Libgen
from configs.config import images
from plugins.utils.work import work
from pyrogram import filters, errors
from plugins.utils.util import getLang, translate
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

DATA = {
    'user_id' : { 'id' : 'data' },
}


# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
