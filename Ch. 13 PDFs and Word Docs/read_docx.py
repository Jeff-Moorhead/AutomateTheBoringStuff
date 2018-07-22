#! python3

import docx


def get_text(file):
    doc = docx.Document(file)
    full_text = [paragraph.text for paragraph in doc.paragraphs]
    return '\n'.join(full_text)
