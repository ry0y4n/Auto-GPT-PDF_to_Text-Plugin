"""This module contains functions for interacting with the Twitter API."""
from __future__ import annotations
from . import AutoGPTPDFToText
import fitz

plugin = AutoGPTPDFToText()

def pdf2txt(pdf_file_path: str, txt_file_path: str) -> str:
    """Convert a PDF file to a text file.
    Args:
        pdf_filen_path (str): The PDF file path.
        txt_filen_path (str): The TXT file path.
    Returns:
        str: The tweet that was posted.
    """

    doc = fitz.open(pdf_file_path) # open a document
    out = open(txt_file_path, "wb") # create a text output
    for page in doc: # iterate the document pages
        text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
        out.write(text) # write text of page
        out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    out.close()

    return f"Success! The PDF file was converted to TXT."