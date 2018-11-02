
from src.mdparser import MDParser
from src.converter import DocConverter

def md2doc(md_path, doc_path):
    mdp  = MDParser()
    parsed_md = mdp.parse(md_path)

    doc_data = DocConverter.convert(parsed_md)
    DocConverter.write(doc_path, doc_data)

