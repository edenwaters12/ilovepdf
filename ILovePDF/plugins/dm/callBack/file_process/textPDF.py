# This module is part of https://github.com/edenwaters12/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 edenwaters12

file_name = "ILovePDF/plugins/dm/callBack/file_process/textPDF.py"

import fitz
from logger import logger


async def textPDF(input_file: str, cDIR: str, data: str) -> (bool, str):
    """
    - It allows you to access the text contained within a PDF file and use it for different purposes.
    For instance, you can search and index the extracted text to make it more easily accessible.
    - PDF to HTML conversion allows you to publish your PDF content online as web pages that are easily accessible and searchable.
    - PDF to JSON, the structured data can be easily extracted and used for various purposes, such as data analysis or populating a database.

    parameter:
        input_file : Here is the path of the file that the user entered
        cDIR       : This is the location of the directory that belongs to the specific user.

    return:
        bool/finished        : Return True when the request is successful
        output_path/finished : This is the path where the output file can be found.
    """
    try:
        if data == "textT":
            output_path = f"{cDIR}/outPut.txt"
            data = "text"
        elif data == "textH":
            output_path = f"{cDIR}/outPut.html"
            data = "html"
        elif data == "textJ":
            output_path = f"{cDIR}/outPut.json"
            data = "json"
        else:
            return False, "NoSuchFormatHere"

        with fitz.open(input_file) as iNPUT:
            with open(output_path, "wb") as oUTPUT:
                for page in iNPUT:
                    text = page.get_text(data).encode("utf8")
                    oUTPUT.write(text)
                    oUTPUT.write(bytes((12,)))

        return True, output_path

    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)
        return False, Error

      # If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
