from docx import Document
from jinja2 import Template
from pydantic import BaseModel
import pandas as pd

class Demo(BaseModel):
    nome: str

if __name__ == "__main__":
    print("Python OK! Libs importadas.")
    doc = Document()
    doc.add_heading("GERADOR-DE-DOCS", 0)
    doc.save("demo.docx")
    print("Gerado demo.docx")
