# 🔍 Simple RAG Pipeline with OpenAI and LangChain

This project demonstrates a minimal Retrieval-Augmented Generation (RAG) pipeline using OpenAI's ChatGPT and FAISS vector search over PDF documents.

## 📁 Project Structure

```
.
├── dataset/            # Folder containing input PDF documents
├── create_index.py     # Script to load PDFs, chunk, embed, and save FAISS index
├── run_rag.py          # Script to interact with the RAG pipeline
├── index.faiss/        # Saved FAISS index (auto-generated)
├── chunks.json         # JSON containing chunk metadata (auto-generated)
└── README.md           # This file
```

---

## ✅ Requirements

Make sure you have Python 3.8 or later.

### 🔧 Installation

Run the following command to install all required dependencies:

```bash
pip install langchain openai faiss-cpu PyMuPDF
```

---

## 🚀 Step-by-Step Usage

### 1. Prepare your PDFs

Place your `.pdf` files inside the `dataset/` folder.

### 2. Generate the FAISS Index

This script:

* Loads and splits your PDFs into chunks
* Generates OpenAI embeddings
* Saves FAISS index and chunk metadata

```bash
python create_index.py
```

Make sure to replace your OpenAI API key in the script:

```python
os.environ['OPENAI_API_KEY'] = 'your_personal_openai_api_key_here'
```

### 3. Ask Questions via RAG Pipeline

Use the RAG pipeline to ask questions about your PDFs:

```bash
python run_rag.py
```

You can now interact with the documents by asking natural language questions. Type `exit` to quit.

---

## 🧠 How It Works

1. **Document Parsing**: `PyMuPDF` loads and splits PDF documents.
2. **Embedding**: `OpenAIEmbeddings` converts each chunk to a vector.
3. **Indexing**: Chunks are stored in a FAISS vector index.
4. **Retrieval**: Given a user query, similar chunks are retrieved.
5. **Answer Generation**: ChatGPT uses those chunks to answer the question.

---

## 📌 Notes

* This is a simple implementation meant for learning and prototyping.
* For production use, consider handling larger files, streaming, and persistent storage.
* Ensure your OpenAI usage follows rate limits and pricing based on token usage.

---


Enjoy building with RAG! 🧠📚
