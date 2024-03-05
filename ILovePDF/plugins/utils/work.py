# This module is part of https://github.com/edenwaters12/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 edenwaters12

file_name = "ILovePDF/plugins/utils/work.py"

from plugins import *
from pyrogram import enums


async def work(
    message, work: str = "check", mtype :bool = True
) -> str:
    """
    program will now create a brand new directory to store all of your important user data depending up on chat_type

    mtype: TRUE if message or FALSE if callbackquery
    work: create, check, delete
    """
    if mtype:
        if message.chat.type == enums.ChatType.PRIVATE:
            path = f"work/edenwaters12/{message.chat.id}"
        else:
            pat = f"work/edenwaters12/{message.chat.id}"
            path = f"work/edenwaters12/{message.chat.id}/{message.from_user.id}"
    else:
        if message.message is None:
            # inline query download cant get message from callback
            path = f"work/edenwaters12/inline{message.data.split('|')[2]}"
        elif message.message.chat.type == enums.ChatType.PRIVATE:
            path = f"work/edenwaters12/{message.message.chat.id}"
        else:
            pat = f"work/edenwaters12/{message.message.chat.id}"
            path = f"work/edenwaters12/{message.message.chat.id}/{message.message.from_user.id}"
    if work == "create":
        if os.path.exists(path):
            return False  # False if work exists
        os.makedirs(path)
        return path
    elif work == "check":
        return path if os.path.exists(path) else False
    elif work == "delete":
        if (
            mtype
            and message.chat.type != enums.ChatType.PRIVATE
            and len(os.listdir(pat)) == 1
        ):
            return shutil.rmtree(pat, ignore_errors=True)
        elif not mtype and message.message is None:
            # inline message
            return shutil.rmtree(path, ignore_errors=True)
        elif (
            not mtype
            and message.message.chat.type != enums.ChatType.PRIVATE
            and len(os.listdir(pat)) == 1
        ):
            return shutil.rmtree(pat, ignore_errors=True)
        return shutil.rmtree(path, ignore_errors=True)

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
