from pdfplumber.pdf import PDF
import pdfminer
import pdfminer.pdftypes
pdfminer.pdftypes.STRICT = False

def load(file_or_buffer, **kwargs):
    return PDF(file_or_buffer, **kwargs)

def from_path(path, **kwargs):
    with open(path, "rb") as f:
        return PDF(f, **kwargs)

def set_debug(debug=0):
    pdfminer.debug = debug

set_debug(0)