import fitz  # PyMuPDF

def read_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = "\n".join([page.get_text() for page in doc])
    else:
        text = uploaded_file.read().decode("utf-8")
    return text.strip()
