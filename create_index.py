import os
import json
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Setup API key
os.environ['OPENAI_API_KEY'] = 'your_personal_openai_api_key_here'

# Load PDFs from dataset folder
dataset_folder = "./dataset"
pdf_files = [os.path.join(dataset_folder, f) for f in os.listdir(dataset_folder) if f.endswith('.pdf')]

documents = []
for pdf in pdf_files:
    loader = PyMuPDFLoader(pdf)
    documents.extend(loader.load())

# Split documents into manageable chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

# Generate embeddings
embeddings = OpenAIEmbeddings()

# Create FAISS vector index
vectorstore = FAISS.from_documents(chunks, embeddings)

# Save FAISS index
vectorstore.save_local("index.faiss")

# Save chunks metadata
chunks_data = [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in chunks]
with open("chunks.json", "w", encoding="utf-8") as f:
    json.dump(chunks_data, f, ensure_ascii=False, indent=4)

print(f"Processed {len(chunks)} chunks.")
