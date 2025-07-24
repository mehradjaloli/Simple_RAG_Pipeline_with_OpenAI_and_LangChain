import os
import json
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# Setup API key
os.environ['OPENAI_API_KEY'] = 'your_personal_openai_api_key_here'

# Load embeddings and index
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local("index.faiss", embeddings)

# Setup RetrievalQA chain
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)
rag = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorstore.as_retriever(search_kwargs={"k": 5})
)

# Ask questions interactively
print("Ask questions (type 'exit' to quit):\n")
while True:
    query = input("Your question: ")
    if query.lower() == 'exit':
        break

    response = rag.run(query)
    print(f"\nAnswer:\n{response}\n")
