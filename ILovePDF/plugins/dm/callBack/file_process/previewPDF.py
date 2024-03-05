# This module is part of https://github.com/edenwaters12/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 edenwaters12

file_name = "ILovePDF/plugins/dm/callBack/file_process/previewPDF.py"

media = {}

import fitz, os
from PIL import Image
from logger import logger
from asyncio import sleep
from pyrogram import enums
from pdf import pyTgLovePDF
from plugins.utils import *
from telebot.types import InputMediaPhoto


async def previewPDF(
    input_file: str, cDIR: str, editMessage, cancel, callbackQuery
) -> (bool, str):
    try:
        """
        This function returns PDF images with their metadata.
        If the PDF has 10 or fewer pages, all pages are included.
        If the PDF has more than 10 pages, the function returns the first three pages,
        the last three pages, and three or four pages from the middle of the document
        depending on whether the document has an odd or even number of pages.

        parameter:
            input_file    : Here is the path of the file that the user entered
            cDIR          : This is the location of the directory that belongs to the specific user.
            editMessage   : edit Message progress bar
            callbackQuery : callbackQuery message

        return:
            "finished"    : Return finished when the request is successful
            "finished"    : Return finished when the request is successful
        """
        with fitz.open(input_file) as iNPUT:

            if iNPUT.page_count <= 10:
                preview = list(range(1, iNPUT.page_count + 1))
            else:
                preview = (
                    [1, 2, 3]
                    + list(range(iNPUT.page_count // 2 - 1, iNPUT.page_count // 2 + 2))
                    + list(range(iNPUT.page_count - 2, iNPUT.page_count + 1))
                )

            pdfMetaData = (
                "".join(
                    f"`{i} : {iNPUT.metadata[i]}`\n"
                    for i in iNPUT.metadata
                    if iNPUT.metadata[i] != ""
                )
                if iNPUT.metadata
                else ""
            )

            await editMessage.edit(
                text=f"`𝚏𝚎𝚝𝚌𝚑𝚒𝚗𝚐 𝚙𝚊𝚐𝚎𝚜: {preview}` 🙇", reply_markup=cancel
            )
            mat = fitz.Matrix(2, 2)
            os.mkdir(f"{cDIR}/pgs")
            for pageNo in preview:
                pix = iNPUT.load_page(int(pageNo) - 1).get_pixmap(matrix=mat)
                # SAVING PREVIEW IMAGE
                with open(f"{cDIR}/pgs/{pageNo}.jpg", "wb"):
                    pix.save(f"{cDIR}/pgs/{pageNo}.jpg")

            directory = f"{cDIR}/pgs"
            imag = [os.path.join(directory, file) for file in os.listdir(directory)]
            imag.sort(key=os.path.getctime)
            media[callbackQuery.message.chat.id] = []

            for file in imag:
                await sleep(0.5)
                qualityRate = 95
                for i in range(200):
                    # FILES WITH 10MB+ SIZE SHOWS AN ERROR FROM TELEGRAM
                    # SO COMPRESS UNTIL IT COMES LESS THAN 10MB.. :(
                    if os.path.getsize(file) >= 1000000:
                        picture = Image.open(file)
                        picture.save(file, "JPEG", optimize=True, quality=qualityRate)
                        qualityRate -= 5
                    # ADDING TO GROUP MEDIA IF POSSIBLE
                    else:
                        if len(media[callbackQuery.message.chat.id]) == 1:
                            media[callbackQuery.message.chat.id].append(
                                InputMediaPhoto(
                                    media=open(file, "rb"),
                                    caption=f"`𝚙𝚊𝚐𝚎𝚜: {preview}`\n\n{pdfMetaData}",
                                    parse_mode="Markdown",
                                )
                            )
                        else:
                            media[callbackQuery.message.chat.id].append(
                                InputMediaPhoto(media=open(file, "rb"))
                            )
                        break

            await editMessage.edit(
                text=f"`𝚞𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚊𝚕𝚋𝚞𝚖: {preview}` 🙇", reply_markup=cancel
            )
            if await work.work(callbackQuery, "check", False):
                await callbackQuery.message.reply_chat_action(
                    enums.ChatAction.UPLOAD_PHOTO
                )
                await pyTgLovePDF.send_media_group(
                    callbackQuery.message.chat.id,
                    media[callbackQuery.message.chat.id],
                    reply_to_message_id=callbackQuery.message.id,
                )
            del media[callbackQuery.message.chat.id]
        return "finished", "finished"

    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)
        return False, Error

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
