import os
import re
from pdf2image import convert_from_path
import pytesseract
from docx import Document

class ResumeReaderAgent:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_resume(self):
        file_extension = os.path.splitext(self.file_path)[-1].lower()
        if file_extension == ".pdf":
            return self._read_pdf()
        elif file_extension == ".docx":
            return self._read_docx()
        else:
            raise ValueError("Unsupported file format. Please use PDF or DOCX.")

    def _read_pdf(self):
        try:
            text = ""
            images = convert_from_path(self.file_path)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            for img in images:
                text += pytesseract.image_to_string(img)
            return self._clean_text(text)
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""

    def _read_docx(self):
        try:
            doc = Document(self.file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return self._clean_text(text)
        except Exception as e:
            print(f"Error reading DOCX: {e}")
            return ""

    def _clean_text(self, text):
        # Basic text cleaning
        return re.sub(r'\s+', ' ', text).strip()
    
def run_agent(file_path):
    reader_agent = ResumeReaderAgent(file_path)
    resume_text = reader_agent.read_resume()
    return resume_text
