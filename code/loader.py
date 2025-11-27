# loader.py
import docx2txt
import os

def load_docx_text(path):
    print("DEBUG PATH RECEIVED BY loader.py:", repr(path))
    print("File exists:", os.path.exists(path))

    text = docx2txt.process(path)

    if not text.strip():
        print("WARNING: DOCX has no extractable text. Try saving a clean version or remove tables.")
    
    return text.strip()

if __name__ == "__main__":
    path = r"D:\RAG_Sanskrit_RohanSoni\data\Rag-docs-fixed.docx"
    print(load_docx_text(path))
