# Smart_Assistant-EZ-
# 🤖 Smart Assistant for Research Summarization

An intelligent local assistant that allows users to upload a research document (PDF/TXT) and interact with it using two powerful modes:

- ✅ **Ask Anything**: Ask free-form questions from the document.
- 🎯 **Challenge Me**: Attempt AI-generated logical/comprehension questions with feedback.
- 📌 **Auto Summary**: Automatically generate a 150-word summary of the uploaded content.

> Built using **Python 3.12**, **Streamlit**, **Transformers**, and **TensorFlow** – no PyTorch used.

---

## 🧰 Features

| Feature               | Description |
|-----------------------|-------------|
| 📄 File Upload        | Supports `.pdf` and `.txt` |
| ✍️ Ask Anything       | Free-form Q&A from document |
| 🧠 Challenge Me       | Auto-generated questions & evaluation |
| 📑 Auto Summary       | 150-word summarization |
| 📚 Contextual Answer  | Justification based on source content |
| 🌐 Local Web UI       | Built with Streamlit |

---

## 🏗️ Architecture & Reasoning Flow

smartAssistantEZ/
├── app.py                     # Streamlit web app interface
├── engine/                    # Core logic and processing modules
│   ├── __init__.py            # Module initializer
│   ├── file_utils.py          # Handles PDF and TXT file reading
│   ├── summarizer.py          # Summarizes uploaded document
│   ├── qa_engine.py           # Q&A engine for "Ask Anything" mode
│   ├── challenge_engine.py    # Generates and evaluates questions in "Challenge Me" mode
├── requirements.txt           # List of dependencies for pip install
└── README.md                  # Project documentation and setup instructions

### 🧠 Reasoning Flow

#### 1. File Upload (PDF/TXT)
- Handled via Streamlit.
- PDF text extracted using **PyMuPDF**.
- TXT read as plain UTF-8 text.

#### 2. Auto Summary
- Runs on upload.
- Uses `google/pegasus-xsum` model via 🤗 `transformers` with TensorFlow backend.
- Trims input to 1024 tokens for efficiency.
- Summary limited to 150 words.

#### 3. Ask Anything Mode
- Uses `distilbert-base-uncased-distilled-squad` for QA via `pipeline("question-answering")`.
- Returns:
  - **Answer**
  - **Justification** (based on context match)

#### 4. Challenge Me Mode
- Uses `valhalla/t5-small-qa-qg-hl` to generate 3 questions from random sentences.
- Evaluates your input with basic scoring and document-backed feedback.
- Simulated evaluation via basic logic for lightweight local execution.

---

## 🖥️ Setup Instructions

> ✅ Python 3.12 required  
> ❌ PyTorch is not required  
> ⚠️ Use only TensorFlow-based models

