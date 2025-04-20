import fitz  
from docx import Document

def extract_text_from_pdf(document):
    document = fitz.open(document)
    text_chunks = [page.get_text() for page in document]
    return text_chunks

def save_to_docx(text_chunks, output_path):
    doc = Document()
    for chunk in text_chunks:
        doc.add_paragraph(chunk)
    doc.save(output_path)
