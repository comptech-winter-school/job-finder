import pdfplumber
from docx import Document


def get_text_from_file(file_path):
    if file_path.endswith('pdf'):
        with pdfplumber.open(file_path) as pdf:
            text = ''
            for p in pdf.pages:
                p_text = p.extract_text()
                text += '\n' + p_text
            print(text)
    elif file_path.endswith('docx'):
        docx = Document(file_path)
        for para in docx.paragraphs:
            print(para.text)
