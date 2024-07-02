from docx import Document


doc = Document("./Parser/DOC/sample1.docx")
for paragraph in doc.paragraphs:
    print(paragraph.text)
    print("\n")
