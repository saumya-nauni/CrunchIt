import pandas as pd
import docx2txt
import slate3k as slate
import re
import fitz

def read_docx(file):
    raw_text = docx2txt.process(file)
    return raw_text

def read_pdf(file):
	if file is not None:
		with fitz.open(stream=file.read(), filetype="pdf") as doc:
			text = ""
			for page in doc:
				text += page.getText()
	return text

