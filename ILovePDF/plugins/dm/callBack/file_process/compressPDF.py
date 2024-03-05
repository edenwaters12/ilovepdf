# This module is part of https://github.com/edenwaters12/ilovepdf
# Feel free to use and contribute to this project. Your contributions are welcome!
# copyright ©️ 2021 edenwaters12

file_name = "ILovePDF/plugins/dm/callBack/file_process/compressPDF.py"

import os
import subprocess
from PIL import Image
from logger import logger
from plugins.utils import *
# from PyPDF2 import PdfReader, PdfWriter

async def compressPDF(
    input_file: str, cDIR: str, returnRatio: bool = False
) -> (bool, str):
    """
    Compressing a PDF file can significantly reduce its file size, making it
    easier to share and store. This can be especially useful when sending files over
    the internet, as smaller file sizes can lead to faster uploading and downloading times.

    parameter:
        input_file : Here is the path of the file that the user entered
        cDIR       : This is the location of the directory that belongs to the specific user.

    return:
        bool        : Return True when the request is successful
        output_path : This is the path where the output file can be found.
    """
    try:
        """
        output_path = f"{cDIR}/outPut.pdf"
        with fitz.open(input_file) as iNPUT:
            with fitz.open() as oUTPUT:
                for pg in range(iNPUT.page_count):
                    iNPUT[pg].get_pixmap().save(f"{cDIR}/temp.png")
                    with Image.open(f"{cDIR}/temp.png") as image:
                        rect = iNPUT[pg].rect
                        oUTPUT.new_page(pno = -1, width = rect.width, height = rect.height)
                        oUTPUT[pg].insert_image(rect = rect, filename = f"{cDIR}/temp.png")
                oUTPUT.save(output_path, garbage = 3, deflate = True)


        reader = PdfReader(input_file)
        writer = PdfWriter()

        for page in reader.pages:
            page.compress_content_streams()  # This is CPU intensive!
            writer.add_page(page)
        writer.remove_images()
        with open(output_path, "wb") as f:
            writer.write(f)
        """
        # /screen, /ebook, /printer, /prepress, and /default.
        output_path = f"{cDIR}/outPut.pdf"

        # Set the Ghostscript command and options to compress the PDF
        gs_command = "gs"
        gs_options = [
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/ebook",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile={}".format(output_path),
            input_file,
        ]

        # Call Ghostscript to compress the PDF
        subprocess.call([gs_command] + gs_options)

        # FILE SIZE COMPARISON (RATIO)
        initialSize = os.path.getsize(input_file)
        compressedSize = os.path.getsize(output_path)
        ratio = (1 - (compressedSize / initialSize)) * 100

        if returnRatio:
            if (initialSize - compressedSize) > 1000000 or ratio >= 5:
                return (
                    [
                        await render.gSF(initialSize),
                        await render.gSF(compressedSize),
                        f"{ratio:.2f}",
                    ],
                    output_path,
                )
            else:
                return False, "cantCompressMore"

        return True, output_path

    except Exception as Error:
        logger.exception("🐞 %s: %s" % (file_name, Error), exc_info=True)
        return False, Error

# If you have any questions or suggestions, please feel free to reach out.
# Together, we can make this project even better, Happy coding!  XD
