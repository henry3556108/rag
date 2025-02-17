import streamlit as st
from langchain.document_loaders import TextLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import Ollama
import os

def initialize_interface():
    st.title("🔍 RAG-based QA System (Ollama)")

def load_documents(folder_path):
    documents = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        loader = TextLoader(file_path)
        documents.extend(loader.load())  # 載入每個文件的內容
    return documents

def create_vectorstore(documents, model_name="mistral"):
    embeddings = OllamaEmbeddings(model=model_name)
    vectorstore = FAISS.from_documents(documents, embeddings)
    return vectorstore.as_retriever()

def initialize_qa_chain(retriever, model_name="deepseek-r1:7b"):
    llm = Ollama(model=model_name)
    return RetrievalQA.from_chain_type(llm, retriever=retriever)

def main():
    initialize_interface()
    documents = load_documents("data")
    retriever = create_vectorstore(documents)
    qa_chain = initialize_qa_chain(retriever)

    query = st.text_input("輸入你的問題：")
    if query:
        response = qa_chain.run(query)
        st.write("💡 回答：", response)

if __name__ == "__main__":
    main()
