from .pdf_to_txt import (
    pdf2txt,
)

# test.pdf is located in auto_gpt_workspace directory
def test_pdf_to_txt():
    assert pdf2txt('test.pdf', 'test.txt')=="Success! The PDF file was converted to a text file."