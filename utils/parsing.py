
import io
from pdfminer.high_level import extract_text as pdf_extract_text
import docx2txt

def extract_text_from_file(uploaded_file) -> str:
    name = uploaded_file.name.lower()
    data = uploaded_file.read()
    uploaded_file.seek(0)
    if name.endswith(".pdf"):
        with io.BytesIO(data) as buf:
            return pdf_extract_text(buf) or ""
    elif name.endswith(".docx"):
        with io.BytesIO(data) as buf:
            return docx2txt.process(buf) or ""
    elif name.endswith(".txt"):
        try:
            return data.decode("utf-8", errors="ignore")
        except Exception:
            return data.decode("latin-1", errors="ignore")
    else:
        try:
            return data.decode("utf-8", errors="ignore")
        except Exception:
            return ""
