# This module is part of https://github.com/edenwaters12/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 edenwaters12

file_name = "ILovePDF/plugins/dm/callBack/file_process/ocrPDF.py"

from logger import logger

try:
    edenwaters12 = False  # Change to False else never work
    import ocrmypdf
except Exception:
    edenwaters12 = True


async def ocrPDF(input_file: str, cDIR: str) -> (bool, str):
    try:
        output_path = f"{cDIR}/outPut.pdf"
        ocrmypdf.ocr(
            input_file=open(input_file, "rb"),
            output_file=open(output_path, "wb"),
            deskew=True,
        )
        return True, output_path

    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)
        return False, Error

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
