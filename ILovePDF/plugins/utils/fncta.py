# This module is part of https://github.com/edenwaters12/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 edenwaters12

file_name = "ILovePDF/plugins/utils/fncta.py"

from plugins import *
from PIL import Image
from configs.db import *
from pyrogram.enums import ChatType
from hachoir.parser import createParser
from configs.config import settings, images
from hachoir.metadata import extractMetadata

if dataBASE.MONGODB_URI:
    from database import db

# return thumbnail height
async def thumbMeta(thumbPath: str) -> str:
    try:
        metadata = extractMetadata(createParser(thumbPath))
        if metadata.has("height"):
            return metadata.get("height")
        else:
            return 0
    except Exception as Error:
        logger.exception("1️⃣: 🐞 %s : %s" % (file_name, Error))


# photo_id -> local image
async def formatThumb(location: str) -> str:
    try:
        height = await thumbMeta(location)
        Image.open(location).convert("RGB").save(location)
        img = Image.open(location)
        img.resize((320, height))
        img.save(location, "JPEG")
        return location
    except Exception as Error:
        logger.exception("2️⃣: 🐞 %s: %s" % (file_name, Error))


# return thumbnail and fileName
async def thumbName(message, fileName: str, getAPI=False) -> str:
    try:
        chat_type = message.chat.type
        chat_id = message.chat.id
        fileNm, fileExt = os.path.splitext(fileName)

        if dataBASE.MONGODB_URI:
            info = await db.get_user_data(chat_id)

        if settings.DEFAULT_NAME:
            FILE_NAME = settings.DEFAULT_NAME + fileExt
        elif dataBASE.MONGODB_URI and info and info.get("fname", 0):
            FILE_NAME = info["fname"] + fileExt
        else:
            FILE_NAME = fileName

        if settings.DEFAULT_CAPT:
            FILE_CAPT = settings.DEFAULT_CAPT
        elif dataBASE.MONGODB_URI and info and info.get("capt", 0):
            FILE_CAPT = info["capt"]
        else:
            FILE_CAPT = ""

        if dataBASE.MONGODB_URI:
            if chat_type == ChatType.PRIVATE and message.chat.id in CUSTOM_THUMBNAIL_U:
                THUMBNAIL = info["thumb"]
            else:
                THUMBNAIL = images.PDF_THUMBNAIL
        else:
            THUMBNAIL = images.PDF_THUMBNAIL

        if not getAPI:
            return FILE_NAME, FILE_CAPT, THUMBNAIL
        else:
            return FILE_NAME, FILE_CAPT, THUMBNAIL, info.get("api", 0)

    except Exception as Error:
        logger.exception("3️⃣: 🐞 %s : %s" % (file_name, Error))


# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
